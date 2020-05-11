from flask import render_template, redirect, request

from . import courses
from .models import Course


@courses.route('/courses')
def listCourses():
    return render_template('courses/list_courses.html')
