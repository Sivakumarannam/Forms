from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.


def insert_topics(request):

    if request.method=='POST':
        topic=request.POST['tp']

        TPO=Topic.objects.get_or_create(topic_name=topic)[0]
        TPO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topics.html',d)
    return render(request,'insert_topics.html')
def insert_webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpages.html',d1)
    return render(request,'insert_webpages.html',d)


def insert_Access_Records(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        an=request.POST['an']
        dd=request.POST['dd']
        au=request.POST['au']
        WO=Webpage.objects.get(name=an)
        AO=AccessRecords.objects.get_or_create(name=WO,date=dd,author=au)[0]
        AO.save()
        QLAO=AccessRecords.objects.all()
        d1={'access':QLAO}
        return render(request,'display_access_records.html',d1)
    return render(request,'insert_Access_Records.html',d)