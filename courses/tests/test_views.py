from django.test import RequestFactory
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from courses.views import *
from mixer.backend.django import mixer
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestViews:

    def test_course_list_authenticated(self):

        path = reverse('courses:list')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = course_list(request)
        assert response.status_code == 200

    def test_course_list_unauthenticated(self):

        path = reverse('courses:list')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = course_list(request)
        assert 'accounts/login' in response.url

    def test_course_detail_with_course(self):

        mixer.blend('courses.Course', pk=1)
        path = reverse('courses:detail', args=[1])
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = course_detail(request, pk=1)
        assert response.status_code == 200

    def test_course_detail_without_course(self):

        path = reverse('courses:detail', args=[1])
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = course_detail(request, pk=1)
        assert response.status_code == 200
        
    def test_course_delete_without_object_course(self):

        c = Client()
        path = reverse('courses:delete', args=[1])
        response = c.get(path)
        assert response.status_code == 404

    def test_course_delete_object_course_confirm_message(self):

        course = mixer.blend('courses.Course', pk=1, name='prueba')
        c = Client()
        path = reverse('courses:delete', args=[1])
        response = c.get(path)
        message = 'seguro que deseas borrar el curso ' + '"'+course.name+'"'
        url = 'courses/borrar/'+str(course.pk)
        assert message.encode() in response.content
        assert url in response.request['PATH_INFO']


    def test_course_delete_object_course(self):

        mixer.blend('courses.Course', pk=1)
        c = Client()
        path = reverse('courses:delete', args=[1])
        response = c.post(path)
        assert 'courses' in response.url
        assert response.status_code == 302
