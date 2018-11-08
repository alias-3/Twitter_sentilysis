from django.shortcuts import render
from django.http import HttpResponse
from . import  twitter_script


def index(request):
	if request.method=="POST" and request.POST.get('query') != "":
		tweet_list = twitter_script.tweets(request.POST.get('query'),request.POST.get('numtweets'))
		pos,neg,net = twitter_script.analysis(tweet_list)
		context = {
			'tweet_list' : tweet_list,
			'pos': (pos*100/int(request.POST.get('numtweets'))),
			'neg': (neg*100/int(request.POST.get('numtweets'))),
			'net': (net*100/int(request.POST.get('numtweets'))),
			't': len(tweet_list)
		}
		return render(request,"index.html",context)
	else: 
		context = {
			'q': request.POST.get('query') 
		}
		return render(request,"index.html",context)