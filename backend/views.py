from django import http
from django.shortcuts import redirect, render
from .models import *
import os
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse

notlist=['@',' ','#', '$', '%', '^', '!', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']', ';', ':', '"', "'", '<', '>', ',', '?', '/', '\\', '~', '`']
textfiles=['txt','sh','text','py','html','css','scss','js','bash','xml','bat']
images=['jpg','png','gif','ico','jpeg']
audio=['mp3','wav','wma',]
video=['mp4']
# Create your views here.
def index(request):
  if request.method == 'POST':
    if request.POST.get('name'):
        name=request.POST.get('name')
        like(name=name).save()
    else:
      like().save()
  s=reversed(files.objects.all())
  return render(request,'home.html',{'uploadedfiles':s,'likes':len(like.objects.all())})

def upload(request):
  if request.method == 'POST' and request.FILES['fileInput']:
    fileObj=request.FILES['fileInput']
    password=request.POST.get('pass')
    fs=FileSystemStorage()
    filename=''
    for let in fileObj.name:
      if let in notlist:
        let='-'
      else:
        pass
      filename=str(filename) + str(let)
    filePathName=fs.save(filename,fileObj)
    filePathName=fs.url(filePathName)
    if password == 'none':
      files(name=filename,file=filePathName[7:]).save()
    else:
      files(name=filename,lock=1,password=password,file=filePathName[7:]).save()
    messages.success(request, 'Your file uploaded successfully')
    return redirect('home')
  return HttpResponse('some error')

def delet(request,idf):
  if files.objects.filter(id=idf)[0].name=='help.txt':
    messages.success(request, 'Soory can delete this file')
    return redirect('home')
  else:
    try:
      os.remove(files.objects.get(id=idf).file.path)
    except:
      pass
    files.objects.filter(id=idf).delete()
    messages.success(request, 'Your file deleted successfully')
    return redirect('home')

def viewfiles(request):
    s=reversed(files.objects.all())
    return render(request,'viewfiels.html',{'uploadedfiles':s,'likes':len(like.objects.all())})


def singleview(request,idf):
  file=files.objects.filter(id=idf)
  dbfil_ex=str(file[0]).split('.')[-1].lower()
  if len(str(file[0])) > 15:
    name=str(file[0])[0:30]+'...'
  else:
    name=file[0]
  if dbfil_ex in textfiles:
    fltype='txt'
    data1=(files.objects.get(id=idf).file.path)
    s=open(data1,'r')
    data=s.readlines()
  elif dbfil_ex in images:
    fltype='img'
    data=(files.objects.filter(id=idf)[0].file.url)
  elif dbfil_ex in audio:
    fltype='music'
    data=(files.objects.filter(id=idf)[0].file.url)
  elif dbfil_ex in video:
    fltype='video'
    data=(files.objects.filter(id=idf)[0].file.url)
  elif dbfil_ex == 'pdf':
    fltype='pdf'
    data=(files.objects.filter(id=idf)[0].file.url)
    parm={
    'filename':name,
    'type':fltype,
    'data':data,
    'likes':len(like.objects.all())
    }
    return render(request,'pdfview.html',parm)
  else:
    fltype='no'
    data=''
  parm={
    'filename':name,
    'type':fltype,
    'data':data,
    'likes':len(like.objects.all())
  }
  return render(request,'singleview.html',parm)


def likes(request):
  return HttpResponse(len(like.objects.all()))

def download(request):
  file_id=request.GET.get('file_id')
  password=request.GET.get('password')
  if files.objects.get(id=file_id).lock == '1':
    userpass=files.objects.get(id=file_id).password
    if password == userpass:
      return HttpResponse(files.objects.get(id=file_id).file.url)
    else:
      return HttpResponse('You have Entered Wrong password.')
  else:
    return HttpResponse(files.objects.get(id=file_id).file.url)

def viewcheck(request):
  file_id=request.GET.get('file_id')
  password=request.GET.get('password')
  if files.objects.get(id=file_id).lock == '1':
    userpass=files.objects.get(id=file_id).password
    if password == userpass:
      return HttpResponse('/view/'+str(file_id))
    else:
      return HttpResponse('You have Entered Wrong password.')
  else:
    return HttpResponse('/view/'+str(file_id))

def deletcheck(request):
  file_id=request.GET.get('file_id')
  password=request.GET.get('password')
  if files.objects.get(id=file_id).lock == '1':
    userpass=files.objects.get(id=file_id).password
    if password == userpass:
      return HttpResponse('/delete/'+str(file_id))
    else:
      return HttpResponse('You have Entered Wrong password.')
  else:
    return HttpResponse('/delete/'+str(file_id))