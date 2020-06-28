from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import MeetingRoom
from .serializers import MeetingRoomsSerializer

# Create your views here.
def meeting(request):
    return render(request, "index.html")

def getMeetingrooms(request):
    results={}
    queryset = MeetingRoom.objects.values().all().order_by('roomNo')
    results=list(queryset)
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