# Generated by Django 2.2.2 on 2019-07-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190714_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.FileField(default='新闻内容', upload_to='', verbose_name='内容'),
        ),
    ]
