from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import MeetingRoom
from .models import Reserve
from .serializers import MeetingRoomsSerializer
import sqlite3

# Create your views here.
def meeting(request):
    return render(request, "index.html")

def getMeetingrooms(request):
    responseFlag = 0
    if request.method == "GET":
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
            responseFlag = 1
            reserve = Reserve(reserveRoomNo=roomNo, reservDate=date, reserveStartTime=startTime, reserveEndTime=endTime, mediaFlg=0, reservePerson=000)
            reserve.save
        
    results={responseFlag}
    return JsonResponse(results, safe=False)

class DataTest(APIView):
    def get(self,request,*args,**kwargs):
        print('请求后台数据成功！')
        return Response(['后台列表数据1','后台列表数据2'])

class Search(APIView):
    def get(self,request):
        kw = request.GET.get('0', None)
        print(request.GET.get('0', None))
        if kw != None:
            return Response("您搜索的数据为：" + kw)
        else:
            return Response("没有搜索到任何数据")
            
class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all().order_by('roomNo')
    serializer_class = MeetingRoomsSerializer