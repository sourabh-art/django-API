from django.shortcuts import render,redirect
import json
from data.models import content,User_data
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models import content,User_data
from data.serializers import contentSerializer,User_dataSerializer
class contentdata(viewsets.ModelViewSet):
    queryset=content.objects.all()
    serializer_class=contentSerializer

class userdata(viewsets.ModelViewSet):
    queryset=User_data.objects.all()
    serializer_class=User_dataSerializer


    
@api_view(["GET"])
def sixdata(request):
    if request.method=="GET":
        s_dat=User_data.objects.all().order_by('-no_of_views')
        serializer=User_dataSerializer(s_dat[0:7],many=True)
        return Response(serializer.data)
  

def home(request):
    return render(request,"home.html")
def input(request):
    if request.method=="POST":
        uplode_file=request.FILES["document"]
        if uplode_file.name=="ContentData.json":
            data1=json.load(uplode_file)
            for i in data1:
                data=content(movie_id=i["movie_id"],movie_name=i["movie_name"],store_id=i["store_id"],alie_customer_id=i["alie_customer_id"])
                data.save()
            return render(request,"home.html")
        
        elif uplode_file.name=="UserData.json":
            data2=json.load(uplode_file)
            for i in data2:
                data=User_data(movie_id=i["movie_id"],user_id=i["user_id"],timestamp=i["timestamp"],user_email=i["user_email"],user_name=i["user_name"],no_of_views=i["no_of_views"],alie_customer_id=i["alie_customer_id"],store_id=i["store_id"])
                data.save()
            return render(request,"home.html")
        else:
            messages.error(request,"Wrong Input")
            return redirect(input)
    
    else:
        return render(request,"input.html")
def data(request):
    user=User_data.objects.all().order_by('-no_of_views')
    parm={"user":user}
    return render(request,"output.html",parm)

