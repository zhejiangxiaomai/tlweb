# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import pytz
# Create your views here.
import json
from db import models
from urllib2 import Request
def DashBoard(request):
	context = {}
	return render(request, 'Member/DashBoard.html', context)

def MsgList(request):
	context = {}
	return render(request, 'Member/MsgList.html', context)

def ShowModel(request):
	context = {}
	return render(request, 'Member/ShowModel.html', context)

def ComBank(request):
	context = {}
	return render(request, 'Member/ComBank.html', context)

def MemberOrder(request):
	member_ = models.OrderForm()
	ordlist, maxPage = member_.myMemberOrder(1,None,None,"1",1)
	for i in ordlist:
		print i.order_id
	print "最多",maxPage
	
	context = {}
	return render(request, 'Member/MemberOrder.html', context)

def RewardOrder(request):
	context = {}
	return render(request, 'Member/RewardOrder.html', context)

def RewardOrderList(request):
	context = {}
	return render(request, 'Member/RewardOrderList.html', context)

def Recome(request):
	context = {}
	return render(request, 'Member/Recome.html', context)

def RecomeList(request):
	context = {}
	return render(request, 'Member/RecomeList.html', context)

def MyRecomeAll(request):
	context = {}
	member_ = models.Member()
	list ,maxPage = member_.myReference(1,1)
	print list
	print "最多",maxPage
	return render(request, 'Member/MyRecomeAll.html', context)

def MyData(request):
	context = {}
	return render(request, 'Member/MyData.html', context)

def Advice(request):
	context = {}
	advice_ = models.Advice()
	#advice_.send_advice(1,"没阅读啊哈哈","内容内容",1)
	#advice_.reply_advice(1,"回复回复",1,6)
	#参数如果没有就要写None作为占位符

	#timezone.now()
	
	
#timezone.now()
	return render(request, 'Member/Advice.html', context)

def AdviceList(request):
	context = {}
	advice_ = models.Advice()
	naive = parse_datetime("2016-03-21 10:28:45")
	time_ = pytz.timezone("UTC").localize(naive, is_dst=None)	
	adlist,maxPage =  advice_.my_advice(1,"0",None,None,time_,timezone.now())
	for i in adlist :
		print i.advice_id
	print "最多",maxPage
	return render(request, 'Member/AdviceList.html', context)