from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import data

COURSE_CHOICES = data.getCourseList()

class CourseForm(FlaskForm):
    course = SelectField(label='Course', choices=COURSE_CHOICES)
    submit = SubmitField('Add Course')