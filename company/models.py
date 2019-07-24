from django.db import models

# Create your models here.

class Images(models.Model):
    status_choice = (
        (0,'上线'),
        (1,'下线'),
    )
    status = models.IntegerField(status_choice,default=1)
    name = models.CharField(max_length=100,unique=True)
    img = models.ImageField(upload_to='./static/images/focus/')
    href = models.CharField(max_length=256)
    create_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Images'
        verbose_name_plural = '首页轮播'

    def __str__(self):
        return self.name


class News(models.Model):
    status_choice = (
        (0,'上线'),
        (1,'下线'),
    )
    status = models.IntegerField(status_choice,default=1)
    weight = models.IntegerField(verbose_name="权重",default=0)
    name = models.CharField(verbose_name='新闻标题',max_length=32,unique=True)
    summary =models.CharField(verbose_name='内容',max_length=1000,default='新闻内容')

    class Meta:
        db_table = 'News'
        verbose_name_plural='首页公告'

    def __str__(self):
        return self.name

class Superman(models.Model):
    status_choice = (
        (0,'上线'),
        (1,'下线'),
    )
    status = models.IntegerField(status_choice,default=1)
    weight = models.IntegerField(verbose_name="权重",default=0)
    img = models.ImageField(upload_to='./static/images/superman/')
    name = models.CharField(verbose_name='村民干部', max_length=32, unique=True)
    summary = models.CharField(verbose_name='简介', max_length=100, default='个人简介')

    class Meta:
        db_table = 'Superman'
        verbose_name_plural='村民干部'

    def __str__(self):
        return self.name


class Direction(models.Model):
    """
    方向：自动化、测试、运维、前端
    """
    name = models.CharField(verbose_name='名称',max_length=32,unique=True)
    classification = models.ManyToManyField('Classification')

    class Meta:
        db_table = 'Direction'
        verbose_name_plural = '方向(视频方向)'

    def __str__(self):
        return self.name

class Classification(models.Model):
    """
    分类：Python Linux Javascript openStack Node.js
    """
    name = models.CharField(verbose_name='名称',max_length=32)

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name

class Level(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'Level'
        verbose_name_plural = '难度等级'

    def __str__(self):
        return self.title

class Vedio(models.Model):
    status_choice = (
        (1,'下线'),
        (2,'上线'),
    )

    status = models.IntegerField(verbose_name='状态',choices=status_choice,default=1)
    level = models.ForeignKey(to=Level,on_delete=None)
    classification = models.ForeignKey(to=Classification,on_delete=None)

    weight = models.IntegerField(verbose_name='权重（从大到小排序）',default=0)
    title = models.CharField(verbose_name='标题',max_length=32)
    img = models.CharField(verbose_name='图片',max_length=32)
    href = models.CharField(verbose_name='视频地址',max_length=256)
    create_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Vedio'
        verbose_name_plural = '视频'

    def __str__(self):
        return self.title

class Imgs(models.Model):

    src = models.ImageField(upload_to="static/images/upload",verbose_name="图片路径")
    name = models.CharField(max_length=32,verbose_name="名字")
    summary = models.CharField(max_length=200,verbose_name="简介")

    class Meta:
        verbose_name_plural = "大湾靓图表"

    def __str__(self):
        return self.name




















