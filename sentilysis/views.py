from django.shortcuts import render
from django.http import HttpResponse
from . import  twitter_script
import json

def index(request):
	if request.method=="POST" and request.POST.get('query') != "":
		tweet_list = twitter_script.tweets(request.POST.get('query'),request.POST.get('numtweets'))
		pos,neg,net,csv_list,pol_dict = twitter_script.analysis(tweet_list)
		context = {
			'tweet_list' : tweet_list,
			'pos': (pos*100/int(request.POST.get('numtweets'))),
			'neg': (neg*100/int(request.POST.get('numtweets'))),
			'net': (net*100/int(request.POST.get('numtweets'))),
			'csv_list' : json.dumps(csv_list),   
			'csv_len' : len(csv_list),
			'pol_dict' : pol_dict,
			't': len(tweet_list)
		}
		return render(request,"index.html",context)
	else: 
		context = {
			'csv_len' : 0,
			'q': request.POST.get('query')
		}
		return render(request,"index.html",context)