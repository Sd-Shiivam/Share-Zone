from django import http
from django.shortcuts import redirect, render
from .models import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home.html',{'uploaded_files':reversed(files.objects.all())})

def upload(request):
  if request.method == 'POST' and request.FILES['fileInput']:
    fileObj=request.FILES['fileInput']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    files(name=fileObj.name,file=filePathName[7:]).save()
    return redirect('home')
  return HttpResponse('some error')

def delet(request,idf):
  files.objects.filter(id=idf).delete()
  return redirect('home')

def viewfiles(request):
    return render(request,'viewfiels.html',{'uploaded_files':reversed(files.objects.all())})
