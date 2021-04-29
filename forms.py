from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField, BooleanField
import data

DEPT_CHOICES = sorted(data.getDepartmentList())
DEPT_CHOICES.insert(0,'ALL DEPTS')
COURSE_CHOICES = data.getCourseList()

class CourseForm(FlaskForm):
    department = SelectField(label='Department', choices = DEPT_CHOICES)
    course = SelectField(label='Course', choices= COURSE_CHOICES)
    submit = SubmitField('Add Course')

class ClearForm(FlaskForm):
    clear = SubmitField('Clear Course Selection')

class StartForm(FlaskForm):
    cb = BooleanField(label="Don't show this again")
    start = SubmitField('Start Planning!')

class RemoveForm(FlaskForm):
    selcourses = SelectMultipleField(label='Selected Courses', choices = [])
    submit = SubmitField('Remove course(s)')

class RecommendForm(FlaskForm):
    mon = BooleanField(label='Monday')
    tues = BooleanField(label='Tuesday')
    wed = BooleanField(label='Wednesday')
    thurs = BooleanField(label='Thursday')
    fri = BooleanField(label='Friday')
    sat = BooleanField(label='Saturday')
    sun = BooleanField(label='Sunday')
    