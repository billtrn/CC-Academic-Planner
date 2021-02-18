from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField
import data

DEPT_CHOICES = data.getDepartmentList()
DEPT_CHOICES.insert(0,'ALL DEPTS')
COURSE_CHOICES = data.getCourseList()

class CourseForm(FlaskForm):
    department = SelectField(label='Department', choices = DEPT_CHOICES)
    course = SelectField(label='Course', choices= COURSE_CHOICES)
    submit = SubmitField('Add Course')

class ClearForm(FlaskForm):
    clear = SubmitField('Clear Course Selection')

class StartForm(FlaskForm):
    start = SubmitField('Start Scheduling!')

class RemoveForm(FlaskForm):
    selcourses = SelectMultipleField(label='Selected Courses', choices = [])
    rem = SubmitField('Remove course(s)')