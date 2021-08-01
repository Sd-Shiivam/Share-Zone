from django import http
from django.shortcuts import redirect, render
from .models import *
import os
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
  if request.method == 'POST':
    if request.POST.get('name'):
        name=request.POST.get('name')
        likeuser(name=name).save()
    likeno=int(like.objects.filter(id=1)[0].likeno)+1
    like(id='1',likeno=likeno).save()
  s=reversed(files.objects.all())
  return render(request,'home.html',{'uploadedfiles':s,'likes':like.objects.filter(id=1)[0].likeno})

def upload(request):
  if request.method == 'POST' and request.FILES['fileInput']:
    fileObj=request.FILES['fileInput']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    files(name=fileObj.name,file=filePathName[7:]).save()
    messages.success(request, 'Your file uploaded successfully')
    return redirect('home')
  return HttpResponse('some error')

def delet(request,idf):
  if files.objects.filter(id=idf)[0].name=='help..txt':
    messages.success(request, 'Soory can delete this file')
    return redirect('home')
  else:
    os.remove(files.objects.get(id=idf).file.path)
    files.objects.filter(id=idf).delete()
    messages.success(request, 'Your file deleted successfully')
    return redirect('home')

def viewfiles(request):
    s=reversed(files.objects.all())
    return render(request,'viewfiels.html',{'uploadedfiles':s,'likes':like.objects.filter(id=1)[0].likeno})


def singleview(request,idf):
  textfiles=['txt','sh','text','py','html','css','scss','js','bash','xml','bat']
  images=['jpg','png','gif','ico','jpeg']
  audio=['mp3','wav','wma',]
  video=['mp4']
  fltype='no'
  data=''
  file=files.objects.filter(id=idf)
  dbfil_ex=str(file[0]).split('.')[-1].lower()
  # print(files.objects.filter(id=idf)[0].file.url)
  if dbfil_ex in textfiles:
    fltype='txt'
    data=(files.objects.filter(id=idf)[0].file).readlines()
  elif dbfil_ex in images:
    fltype='img'
    data=(files.objects.filter(id=idf)[0].file.url)
  elif dbfil_ex in audio:
    fltype='music'
    data=(files.objects.filter(id=idf)[0].file.url)
  elif dbfil_ex in video:
    fltype='video'
    data=(files.objects.filter(id=idf)[0].file.url)
  else:
    pass
  if len(str(file[0])) > 15:
    name=str(file[0])[0:30]+'...'
  else:
    name=file[0]
  parm={
    'filename':name,
    'type':fltype,
    'data':data,
    'likes':like.objects.filter(id=1)[0].likeno
  }
  return render(request,'singleview.html',parm)
def likes(request):
  return HttpResponse(like.objects.filter(id=1)[0].likeno)