from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.meeting, name = "meeting"),
    path("api/meetingrooms", view=views.getMeetingrooms, name="meetingroom_list"),
    path('DataTest/',views.DataTest.as_view()),
    path('Search/',views.Search.as_view()),
]