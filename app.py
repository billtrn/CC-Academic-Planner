from flask import Flask, render_template, jsonify, request, redirect, url_for, session, make_response
from forms import CourseForm, ClearForm, StartForm, RemoveForm
#from flask_cas import CAS
import data
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '9ea87e4f94007164efd29eab1793d57f'

#function to format form.course.data into a dictionary of data for the course
def fmat(course):
    split = course.split("  ")

    dept = split[0]
    num = split[1]
    title = split[2]
    sect = split[3]
    crn = data.getCRN(dept, num, sect)
    days = data.getDays(crn)
    times = data.getTimes(crn)

    #gets rid of any duplicate day/time pairs due to the use of multiple classrooms
    for i in range(len(days)-1):
        for j in range(i+1,len(days)):
            if days[i] == days[j] and times[i] == times[j]:
                del days[j]
                del times[j]

    return {"title": title, "sect": sect, "crn": crn, "dept": dept, "number": num, "days": days, "times": times}

#function to check if the course has a conflict with an already selected course
def conflict(course, courses):
    conflicts = []
    
    #loop through each pre-selected course
    for c in courses:
        
        #loop through the groupings of days for the course being added
        for x in range(len(course["days"])):
            
            #loop through the groupings of days for the pre-selected course
            for y in range(len(c["days"])):
            
                #if the two groupings do not share a day, no need to check for time conflict
                intersection = set(course["days"][x]).intersection(set(c["days"][y]))
                
                if len(intersection) == 0 or intersection == {' '}:
                    continue

                #check for time conflict
                else:

                    #get the time for the xth grouping of days for the course being added
                    t1 = course["times"][x].split("-")

                    #split t1 into start and end times
                    start1 = int(t1[0])
                    end1 = int(t1[1])

                    #get the time for the yth grouping of days for the course being added
                    t2 = c["times"][y].split("-")

                    #split t2 into start and end times
                    start2 = int(t2[0])
                    end2 = int(t2[1])
                    
                    #sort the two time intervals and return True (i.e. there is a conflict) if they overlap
                    r = sorted([[start1,end1],[start2,end2]])
                    if(not (r[0][1] < r[1][0] or r[1][1] < r[0][0])):
                        conflicts.append(c["dept"] + " " + c["number"] + " section " + c["sect"])
    
    return conflicts

@app.route("/how-to", methods=['GET', 'POST'])
def howto():
    return render_template('howto.html', title='How To')

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')

@app.route("/", methods=['GET', 'POST'])
@app.route("/calendar", methods=['GET', 'POST'])
def calendar():
    conf = ""

    #cookies
    cookies = request.cookies
    if "courses" in cookies:
        cs = json.loads(cookies.get("courses"))
    else:
        cs = []

    if "credits" in cookies:
        credits = json.loads(cookies.get("credits"))
    else:
        credits = 0
        for i in cs:
            credits += data.getCredits(i["crn"])

    if "modal" in cookies:
        m = json.loads(cookies.get("modal"))
    else:
        m = "first"
    
    modalform = StartForm()

    form = CourseForm()
    if form.department.data == None:
        form.course.choices = data.getDeptCourses('ALL DEPTS')
    else:
        form.course.choices = data.getDeptCourses(form.department.data)
    form_clear = ClearForm()
    form_remove = RemoveForm()
    
    ch = []
    #for c in courses:
    for c in cs:
        ch.append((c["crn"],(c["title"] + " " + c["sect"])))
        form_remove.selcourses.choices = ch
    
    error = None


    #if the form is submitted validly
    if request.method == 'POST':
        if form.validate_on_submit():
            #reformat the form data into a dictionary of course info
            course = fmat(form.course.data)

            #if the course does not conflict with any pre-selected classes, add it to the class schedule
            conflicts = conflict(course, cs)
            if len(conflicts) == 0:
                #courses.append(course)
                cs.append(course)
                form_remove.selcourses.choices.append((course["crn"],(course["title"] + " " + course["sect"])))
                credits += data.getCredits(course["crn"])

            #if there are one or more conflicts with the current class schedule, do not add it and report conflict
            else:
                conlist = ", ".join(conflicts)
                conf = course["dept"] + " " + course["number"]
                error = 'The selected class, ' + course["title"] + ' (' + ''.join(course["days"]) + ', ' + ''.join(course["times"]) + '),' + ' conflicts with the following courses on your schedule: ' + conlist
        
        if form_remove.submit.data:
            print(form_remove.selcourses.data)
            for s in form_remove.selcourses.data:
                print(cs)
                for i in cs:
                    if i["crn"] == int(s):
                        print("yes")
                        cs.remove(i)
                        form_remove.selcourses.choices.remove((int(s), (i["title"] + " " + i["sect"])))
                        credits -= data.getCredits(i["crn"])
        

        if modalform.start.data:
            if m == "first":
                m = "yes"
            else:
                m = "no"

    attr = []
    for i in cs:
        attr.extend(data.getAttr(i["crn"]))
    attr = ", ".join(list(set(attr)))
    
    res = make_response(render_template('calendar.html', title='Calendar', modalform=modalform, form=form, cform = form_clear, rform = form_remove, error=error, courses=cs, creds=credits, attributes=attr, conf=conf, m=m))
    res.set_cookie("courses", json.dumps(cs))
    res.set_cookie("credits", json.dumps(credits))
    res.set_cookie("modal", json.dumps(m))
    
    return res

@app.route('/course/<dept>')
def course(dept):
    if dept == 'ALL%20DEPTS':
        dept = 'ALL DEPTS'
    cs = data.getDeptCourses(dept)
    return jsonify({'courses' : cs})

if __name__ == "__main__":
    app.run(debug=True)