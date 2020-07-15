from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import MeetingRoom
from .models import Reserve
from .serializers import MeetingRoomsSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import sqlite3

# Create your views here.
def meeting(request):
    return render(request, "index.html")

def getMeetingrooms(request):
    if request.method == "GET":
        orderFlag = 0
        conn = conn=sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        startTime = request.GET.get("startTime")
        endTime = request.GET.get("endTime")
        date = request.GET.get("date")
        roomNo = request.GET.get("roomNo")
        sql = """select * from ReserveRoom where %s=reserveRoomNo and %s=reservDate and(%s between reserveStartTime and reserveEndTime
        or %s between reserveStartTime and reserveEndTime or %s<reserveStartTime and %s>reserveEndTime)"""
        info = (roomNo, date, startTime, endTime, startTime, endTime)
        cursor.execute(sql, info)
        resultRow = cursor.fetchall
        if resultRow == null:
            orderFlag = 1
            reserve = Reserve(reserveRoomNo=roomNo, reservDate=date, reserveStartTime=startTime, reserveEndTime=endTime, mediaFlg=0, reservePerson=000)
            reserve.save
        
    return JsonResponse({
                "orderFlag": orderFlag,
            })
            
class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all().order_by('roomNo')
    serializer_class = MeetingRoomsSerializer

class Users:
    @staticmethod
    def get_status(request):
        if request.user.is_authenticated:
            return JsonResponse({
                "status": 0,
                "username": str(request.user),
                "email": str(request.user.email),
            })
        else:
            return JsonResponse({
                "status": 1
            })

    @staticmethod
    def login_user(request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            if username is not None and password is not None:
                islogin = authenticate(request, username=username, password=password)
                if islogin:
                    login(request, islogin)
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "username": username
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "登录失败, 请检查用户名或者密码是否输入正确."
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })

    @staticmethod
    def logout_user(request):
        logout(request)
        return JsonResponse({
            "status": 0
        })