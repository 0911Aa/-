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


def video2(request,*args,**kwargs):
    condition = {}   #是vedio筛选的条件组成的字典，筛选条件包括direction_id、classification_id、level_id

    for k,v in kwargs.items():  #把传过来的字符串变成数字
        temp = int(v)
        kwargs[k] = temp    #(?P<direction_id>(\d+))-(?P<classification_id>(\d+))-(?P<level_id>(\d+))
    print(kwargs)
# 下面开始构造查询字典
    direction_id = kwargs.get("direction_id")
    classification_id = kwargs.get("classification_id")
    level_id = kwargs.get("level_id")

    direction_list = models.Direction.objects.all()
    """
    如果 direction_id==0
          就显示所有的分类
          如果classification_id == 0
               pass
          否则
               condition["classification_id"]=classification_id
          
    如果 direction_id！=0
          列出当前方向下所有的分类
          如果classification_id == 0
               获取当前方向下所有的分类，比如[1,2,3]，然后赋值
               condition["classification_id__in"]=[1,2,3]
          如果classification_id ！= 0
            获取当前方向下所有分类，比如[1,2,3]
            判断classification_id是否在[1,2,3]中
            如果在：
                condition["classification_id"]=classification_id
            如果不在：
                kwargs['classification_id']赋值为0
                condition["classification_id__in"]=[1,2,3]
               
          
    """
    if direction_id == 0:
        class_list = models.Classification.objects.all()
        if classification_id == 0:
            pass
        else:
            condition["classification_id"]=classification_id


    else:
        direction_obj = models.Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()    #多对多可用,获取queryset对象

        vlist = direction_obj.classification.all().values_list('id')  # 获取对象对应的id值
        if vlist:
            classification_id_list = list(zip(*vlist))[0]  # 转换格式
        else:
            classification_id_list = []

        if classification_id == 0:

            condition["classification_id__in"] = classification_id_list
        else:
            if classification_id in classification_id_list:  #如果两个方向包含同一个被选中的分类，那就继续选中这个分类
                condition["classification_id"] = classification_id
            else:   #否则，就回到全部
                kwargs["classification_id"] = 0
                condition["classification_id"] = classification_id_list

    if level_id == 0:
        pass
    else:
        condition["level_id"] = level_id

    level_list = models.Level.objects.all()
    print('******',condition)
    vedio_list = models.Vedio.objects.filter(**condition)

    return render(request,'vedio2.html',
                  {
                      "kwargs":kwargs,
                      "direction_list":direction_list,
                      "class_list":class_list,
                      "level_list":level_list,
                      "vedio_list":vedio_list,
                  })