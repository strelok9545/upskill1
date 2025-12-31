from django.urls import path
from .views import IndexView,Aboutview,Courseview,CourseDetail

app_name = 'upskill'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('subject/<slug:subject__slug>',IndexView.as_view(),name='courses_of_subject'),
    path('about/',Aboutview.as_view(),name='about'),
    path('courses/',Courseview.as_view(),name='courses'),
    path('course/<slug:slug>detail/',CourseDetail.as_view(),name='detail')
]