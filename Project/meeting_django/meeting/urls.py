from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.meeting, name = "meeting"),
    path("apis/meetingrooms", view=views.getMeetingrooms, name="meetingroom_list") # 会议室列表,
    path('apis/user/login', views.Users.login_user),  # 登录
    path('apis/user/logout', views.Users.logout_user),  # 注销
    path('apis/user/getstatus', views.Users.get_status),  # 返回状态 是否登录
    path('apis/orderMeetingroom', views.getMeetingrooms),  # 返回状态 是否可以预约
]