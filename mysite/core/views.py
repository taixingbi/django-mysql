import os
import json

import logging
logger = logging.getLogger(__name__)

from django.http import Http404
from django.http import HttpResponseServerError
from django.core.exceptions import EmptyResultSet

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.http import JsonResponse
from django.utils import timezone
# from django.contrib.staticfiles import finders
from django.views.decorators.csrf import csrf_exempt

from .utils.botoS3 import s3Bucket

 #db
from .db.read import DBRead


from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

import time



dataTime= {
    "time": timezone.localtime(),
}


# views
class Home(TemplateView):
    template_name = 'home.html'

#logout
def logout_view(request):
    logout(request)
    return render(request,'home.html')

# -----------------------------------------for api-------------------------------------
class ApiReport(): 
    @csrf_exempt  
    def boto(request):  #download cnn model and audio
       
        data= {
            "time": timezone.localtime(),
        }
        
        return JsonResponse(data)

    @csrf_exempt
    def advocateAlert(request):  #test load keras model
        data={
            "test": "rows",
        }

        return JsonResponse(data)

    #test
    @csrf_exempt
    def test(request):
        print("\n\n*************************************api test*************************************")
        rows= DBRead().alert()

        data={
            "test:": rows,
        }
        return JsonResponse(data)