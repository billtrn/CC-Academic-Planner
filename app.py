from flask import Flask, render_template, jsonify, request, redirect, url_for
from forms import CourseForm, ClearForm, StartForm, RemoveForm
import data

app = Flask(__name__)

app.config['SECRET_KEY'] = '9ea87e4f94007164efd29eab1793d57f'
app.config['TEMPLATES_AUTO_RELOAD'] = True

courses = []

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

    return {"title": title, "crn": crn, "dept": dept, "number": num, "days": days, "times": times}

#function to check if the course has a conflict with an already selected course
def conflict(course):
    #if no courses have been added yet, no conflicts
    if len(courses) == 0:
        return False
    
    #check for conflict

    #loop through each pre-selected course
    for c in courses:

        #loop through the groupings of days for the course being added
        for x in range(len(course["days"])):

            #loop through the groupings of days for the pre-selected course
            for y in range(len(c["days"])):

                #if the two groupings do not share a day, no need to check for time conflict
                if len(set(course["days"][x]).intersection(set(c["days"][y]))) == 0:
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
                        return True
    
    #no conflict was found, return False
    return False

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = StartForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('calendar'))
    return render_template('home.html', title='Home', form=form)

@app.route("/calendar", methods=['GET', 'POST'])
def calendar():
    global courses
    form = CourseForm()
    if form.department.data == None:
        form.course.choices = data.getDeptCourses('ALL DEPTS')
    else:
        form.course.choices = data.getDeptCourses(form.department.data)
    form_clear = ClearForm()
    form_remove = RemoveForm()
    ch = []
    for c in courses:
        ch.append((c["title"],c["title"]))
        form_remove.selcourses.choices = ch
    error = None

    #if the form is submitted validly
    if request.method == 'POST':
        if form.validate_on_submit():
            #reformat the form data into a dictionary of course info
            course = fmat(form.course.data)

            #if the course does not conflict with any pre-selected classes, add it to the class schedule
            if conflict(course) is False:
                courses.append(course)
                form_remove.selcourses.choices.append((course["title"],course["title"]))

            #if there are one or more conflicts with the current class schedule, do not add it and report conflict
            else:
                error = 'The selected class, ' + course["title"] + ' (' + ''.join(course["days"]) + ', ' + ''.join(course["times"]) + '),' + ' conflicts with one or more classes in your current schedule.'

        if form_clear.validate_on_submit():
            if form_clear.clear.data:
                courses = []
        
        if form_remove.validate_on_submit():
            if form_remove.rem.data:
                for s in form_remove.selcourses.data:
                    for i in courses:
                        if i["title"] == s:
                            courses.remove(i)
                            form_remove.selcourses.choices.remove((s,s))

    return render_template('calendar.html', title='Calendar', form=form, cform = form_clear, rform = form_remove, courses=courses, error=error)

@app.route('/course/<dept>')
def course(dept):
    cs = data.getDeptCourses(dept)
    return jsonify({'courses' : cs})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')