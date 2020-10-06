from flask import Flask, render_template, flash, redirect, url_for
from forms import CourseForm
import data

app = Flask(__name__)

app.config['SECRET_KEY'] = '9ea87e4f94007164efd29eab1793d57f'

courses = []

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = CourseForm()
    if form.validate_on_submit():
        flash(f'You added {form.course.data}!', 'success')
        courses.append(form.course.data)
        return redirect(url_for('calendar'))
    return render_template('home.html', title='Home', form=form)

@app.route("/calendar", methods=['GET', 'POST'])
def calendar():
    form = CourseForm()
    if form.validate_on_submit():
        flash(f'You added {form.course.data}!', 'success')
        courses.append(form.course.data)
    return render_template('calendar.html', title='Calendar', form=form, courses=courses)

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.209')