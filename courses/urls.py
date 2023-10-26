# from django.conf.urls import url
from django.urls import include, re_path
from .views import *
#from . import views

app_name = "courses"

urlpatterns = [
    re_path(r'^$', course_list, name="list"),
    re_path(r'^(?P<pk>\d+)$', course_detail, name="detail"),
    re_path(r'^nuevo$', CourseCreation.as_view(), name="new"),
    re_path(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name="edit"),
    re_path(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name="delete"),

]
