# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500)

    @property
    def is_available(self):
        date = timezone.now()
        if self.start_date <= date and date <= self.end_date:
            return True
        else:
            return False

    def definitive_score(self, exam1, weighing1, exam2, weighing2):
        try:
            definitive_score = ((exam1*weighing1)+(exam2*weighing2))/100
            return definitive_score
        except Exception as error:
            return error


class Student():
    def approval_percentaje(self, score, scale):
        try:
            percentaje = (score*100)/scale
            return percentaje
        except Exception as error:
            return error

    def student_registration(self, course):
        if course.is_available:
            return "Estudiante puede matricularse"
        else:
            return "Estudiante no se puede matricular"
