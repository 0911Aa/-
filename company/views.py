from django.shortcuts import render,HttpResponse
from company import models

# Create your views here.

def header(request):
    img_list = models.Images.objects.filter(status=1)
    new_list = models.News.objects.filter(status=1)
    superman_list = models.Superman.objects.filter(status=1)
    return render(request,'header.html',
                  {'img_list':img_list,
                  'new_list':new_list,
                   'superman_list':superman_list,
                   }

                  )


def test(request):
    return render(request,'test.html')

def video(request,*args,**kwargs):
    condition = {}     #里面放的是等级id，类别id

    for k,v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp
        if temp:
            condition[k] = temp

    print('kwargs',kwargs)
    print('condition',condition)
    class_list = models.Classification.objects.all()
    level_list = models.Level.objects.all()
    status_list = list(map(lambda x:{'id':x[0],'name':x[1]},models.Vedio.status_choice))
    print(status_list)
    vedio_list = models.Vedio.objects.filter(**condition)
    return render(request,'vedio.html',
                  {
                      'class_list':class_list,
                      'level_list':level_list,
                      'status_list':status_list,
                      'kwargs':kwargs,
                      'vedio_list':vedio_list,
                  })