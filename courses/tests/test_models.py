# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import mock
from mixer.backend.django import mixer
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
import pytest
from courses.models import *


@pytest.mark.django_db
class TestModels:

    def test_course_is_available(self):
        start_date = make_aware(datetime.strptime("2023-10-01", "%Y-%m-%d"))
        end_date = make_aware(datetime.strptime("2023-10-31", "%Y-%m-%d"))
        course = mixer.blend(
            'courses.Course', start_date=start_date, end_date=end_date)
        assert course.is_available == True

    def test_course_is_not_available(self):
        start_date = make_aware(datetime.strptime("2023-10-01", "%Y-%m-%d"))
        end_date = make_aware(datetime.strptime("2023-10-27", "%Y-%m-%d"))
        course = mixer.blend(
            'courses.Course', start_date=start_date, end_date=end_date)
        assert course.is_available == False

    def test_calculate_approval_percentaje(self):
        student = Student()
        score_correct = 4.0
        score_string = '3'
        score_zero = 0
        scale_correct_5 = 5
        scale_correct_10 = 10
        scale_string = '1 - 10'
        scale_zero = 0
        assert student.approval_percentaje(
            score_correct, scale_correct_5) == 80
        assert student.approval_percentaje(
            score_correct, scale_correct_10) == 40
        assert student.approval_percentaje(
            score_string, scale_correct_5).args[0] == "unsupported operand type(s) for /: 'str' and 'int'"
        assert student.approval_percentaje(score_zero, scale_correct_5) == 0
        assert student.approval_percentaje(
            score_correct, scale_string).args[0] == "unsupported operand type(s) for /: 'float' and 'str'"
        assert student.approval_percentaje(
            score_correct, scale_zero).args[0] == "float division by zero"

    def test_definitive_score(self):
        course = mixer.blend('courses.Course')
        exam1 = 3.0
        weighing1 = 50
        exam2 = 4.0
        weighing2 = 50
        assert course.definitive_score(
            exam1, weighing1, exam2, weighing2) == 3.5
        assert course.definitive_score(
            '3', weighing1, exam2, weighing2).args[0] == 'can only concatenate str (not "float") to str'
        assert course.definitive_score(
            exam1, '50', exam2, weighing2).args[0] == "can't multiply sequence by non-int of type 'float'"
        assert course.definitive_score(
            exam1, weighing1, '4', weighing2).args[0] == "unsupported operand type(s) for +: 'float' and 'str'"
        assert course.definitive_score(
            exam1, weighing1, exam2, '50').args[0] == "can't multiply sequence by non-int of type 'float'"
        assert course.definitive_score(exam1, 100, 0, 0) == 3.0

    def test_student_registration(self):
        course_available = mock.Mock(Course)
        course_not_available = mock.Mock(Course)

        course_available.is_available = True
        course_not_available.is_available = False

        student = Student()

        assert student.student_registration(
            course_available) == "Estudiante puede matricularse"
        assert student.student_registration(
            course_not_available) == "Estudiante no se puede matricular"

    def test_approved_course(self):
        student_approved = mock.Mock(Student)
        student_not_approved = mock.Mock(Student)

        student_approved.approval_percentaje = 90
        student_not_approved.approval_percentaje = 89

        student = Student()

        assert student.approved_course(
            student_approved) == "El estudiante aprobo el curso"
        assert student.approved_course(
            student_not_approved) == "El estudiante no aprobo el curso"
