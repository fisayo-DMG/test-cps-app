from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.student_list, name='student_list'),
	url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
]