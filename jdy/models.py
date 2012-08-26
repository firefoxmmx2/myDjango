# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Qyryjbxx(models.Model):
    '''从业人员基本信息，使用支撑平台的，这里只是用来建模的时候临时使用的'''
    qyryid=models.AutoField(primary_key=True,max_length=9) #从业人员ID
    qyrybm=models.CharField(max_length=24) #从业人员编码
class Rdrjbxx(models.Model):
    '''寄件人收件人信息'''
    rdrjbxx_id=models.AutoField(primary_key=True,max_length=9) #寄件人收件人主键 
    xm=models.CharField(max_length=30) #姓名
    zjhm=models.CharField(max_length=18) #证件号码
    ssx=models.CharField(max_length=6) #省市县地址
    xxdz=models.CharField(max_length=120) #详细地址
    lxdh=models.CharField(max_length=20) #联系电话
    gddh=models.CharField(max_length=20,blank=True,null=True) #固定电话
    dw=models.CharField(max_length=60,blank=True,null=True) #单位

class Jdpxx(models.Model):
    '''寄递品信息'''
    jdplx=models.CharField(max_length=3) #寄递品类型
    jdpmc=models.CharField(max_length=120,blank=True,null=True) #寄递品名称
    jdpsm=models.IntegerField(max_length=10) #寄递品数目
    ljjbxx=models.ForeignKey("Ljjbxx",related_name='jpd_set') #关联的揽件信息实体
    jdptj=models.CharField(max_length=30) #寄递品体积
    jdpzl=models.CharField(max_length=30) #寄递品重量
class Ljjbxx(models.Model):
    '''揽件基本信息'''
    djxh=models.CharField(max_length=24,primary_key=True) #登记序号 主键
    jjr=models.ForeignKey(Rdrjbxx,related_name='jjr_set') #寄件人实体，关联寄件人收件人实体
    sjr=models.ForeignKey(Rdrjbxx,related_name="sjr_set") #收件人实体，关联寄件人收件人实体
    ljr=models.ForeignKey(Qyryjbxx,related_name='ljr_set') #揽件人 （从业人员实体）
    ljsj=models.DateField() #揽件时间 年月日 
    ljtbsj=models.DateField() #揽件填报时间 年月日 默认当前时间
    ljtbr=models.ForeignKey(Qyryjbxx,related_name='ljbtr_set') #揽件填报人 关联从业人员实体 默认为当前用户
    sfscbz=models.CharField(max_length=1,default='N',blank=True) #是否删除标识
    sfbz=models.CharField(max_length=1,default='N',blank=True) #是否是补充的揽件信息标识
class Pjjbxx(models.Model):
    '''派件基本信息'''
    ljjbxx=models.ForeignKey(Ljjbxx) #派件关联的揽件信息 揽件实体
    dsrxm=models.CharField(max_length=30,blank=True,null=True) #代收人姓名
    dsrzjlx=models.CharField(max_length=2,blank=True,null=True) #代收人证件类型
    dsrzjhm=models.CharField(max_length=18,blank=True,null=True) #代收人证件号码
    pjr=models.ForeignKey(Qyryjbxx,related_name='pjr_set') #派件人 关联从业人员实体
    pjsj=models.DateField() #派件时间 年月日
    pjtbr=models.ForeignKey(Qyryjbxx,related_name="pjtbr_set") #派件填报人 关联从业人员实体
    pjtbsj=models.DateField() #派件填报时间 年月日
    sfscbz=models.CharField(max_length=1,blank=True,default='N') #是否删除标识

class Kyjdwpxx(models.Model):
    '''可疑寄递物品信息'''
    kyywdjxh=models.CharField(max_length=24) #可疑业务登记序号 主键
    wldh=models.CharField(max_length=40) #物流单号
    kywpms=models.CharField(max_length=120) #可疑物品描述
    kywplb=models.CharField(max_length=2) #可疑物品类别
    bgr=models.ForeignKey(Qyryjbxx,related_name='bgr_set') #报告人 关联从业人员信息
    bgsj=models.DateField(blank=True,null=True) #报告时间 年月日
    sfxcbz=models.CharField(max_length=1,default='N',blank=True) #是否删除标识


