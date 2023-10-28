# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mixer.backend.django import mixer
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
import pytest


@pytest.mark.django_db
class TestModels:

    def test_course_is_available(self):
        start_date = make_aware(datetime.strptime("2023-10-01", "%Y-%m-%d"))
        end_date = make_aware(datetime.strptime("2023-10-31", "%Y-%m-%d"))
        course = mixer.blend('courses.Course', start_date=start_date, end_date=end_date)
        assert course.is_available == True

    def test_course_is_not_available(self):
        start_date = make_aware(datetime.strptime("2023-10-01", "%Y-%m-%d"))
        end_date = make_aware(datetime.strptime("2023-10-27", "%Y-%m-%d"))
        course = mixer.blend('courses.Course', start_date=start_date, end_date=end_date)
        assert course.is_available == False