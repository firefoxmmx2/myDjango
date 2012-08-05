# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    '''系统用户'''
    username=models.CharField(max_length=30)
    useraccout=models.CharField(max_length=30)
    
class Qyryjbxx(models.Model):
    '''从业人员基本信息'''
    qyryid=models.IntegerField(max_length=9)
class Rdrjbxx(models.Model):
    '''寄件人收件人信息'''
    xm=models.CharField(max_length=30)
    zjhm=models.CharField(max_length=18)
    ssx=models.CharField(max_length=6)
    xxdz=models.CharField(max_length=120)
    lxdh=models.CharField(max_length=20)
    gddh=models.CharField(max_length=20,blank=True,null=True)
    dw=models.CharField(max_length=60)

class Jdpxx(models.Model):
    '''寄递品信息'''
    jdplx=models.CharField(max_length=3)
    jdpmc=models.CharField(max_length=120,blank=True,null=True)
    jdpsm=models.IntegerField(max_length=10)
    ljjbxx=models.ForeignKey("Ljjbxx")
class Ljjbxx(models.Model):
    '''揽件基本信息'''
    djxh=models.CharField(max_length=24)
    jjr=models.ForeignKey(Rdrjbxx,related_name='jjr_set')
    sjr=models.ForeignKey(Rdrjbxx,related_name="sjr_set")
    ljr=models.ForeignKey(Qyryjbxx)
    ljsj=models.DateField()
    ljtbsj=models.DateField()
    lttbr=models.ForeignKey(User,)
class Pjjbxx(models.Model):
    '''派件基本信息'''
    ljjbxx=models.ForeignKey(Ljjbxx)
    dsrxm=models.CharField(max_length=30)
    dsrzjlx=models.CharField(max_length=2)
    dsrzjhm=models.CharField(max_length=18)
    pjr=models.ForeignKey(Qyryjbxx,related_name='pjr_set')
    pjsj=models.DateField()
    pjtbr=models.ForeignKey(Qyryjbxx,related_name="+")
    pjtbsj=models.DateField()

class Kyjdwpxx(models.Model):
    '''可疑寄递物品信息'''
    kyywdjxh=models.CharField(max_length=24)
    kdywdjxh=models.CharField(max_length=24)
    wldh=models.CharField(max_length=40)
    kywpms=models.CharField(max_length=120)
    kywplb=models.CharField(max_length=2)
    bgr=models.ForeignKey(Qyryjbxx,related_name='bgr_set')
    bgsj=models.DateField(blank=True,null=True)
    