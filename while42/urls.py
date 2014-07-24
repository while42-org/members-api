from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from while42 import views

urlpatterns = patterns('',
    url(r'^members/$', views.MemberList.as_view()),
    url(r'^members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
    url(r'^chapters/$', views.ChapterList.as_view()),
    url(r'^chapters/(?P<pk>[0-9]+)/$', views.ChapterDetail.as_view()),
    url(r'^random/(?P<pk>[0-9]+)/$', views.RandomMember.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)