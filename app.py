from flask import Flask, render_template, flash, redirect, url_for
from forms import CourseForm
import json
import data

app = Flask(__name__)

app.config['SECRET_KEY'] = '9ea87e4f94007164efd29eab1793d57f'
app.config['TEMPLATES_AUTO_RELOAD'] = True

courses = []

def fmat(course):
    title = (course.split(","))[0]
    crn = data.getCRN(title)
    days = data.getDays(crn)
    times = data.getTimes(crn)
    return {"title": title, "crn": crn, "days": days, "times": times}

def conflict(course):
    return False


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = CourseForm()
    if form.validate_on_submit():
        course = fmat(form.course.data)
        if conflict(course) is False:
            courses.append(course)
            return redirect(url_for('calendar'))
    return render_template('home.html', title='Home', form=form)

@app.route("/calendar", methods=['GET', 'POST'])
def calendar():
    form = CourseForm()
    if form.validate_on_submit():
        courses.append(fmat(form.course.data))
    return render_template('scratchcalendar.html', title='Calendar', form=form, courses=courses)

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.209')

#192.168.1.209