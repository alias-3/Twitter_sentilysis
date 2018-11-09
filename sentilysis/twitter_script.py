import tweepy
from textblob import TextBlob
from . import authenticate
import re


def clean_tweet(tweet):

    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def tweets(query,cnt=20):
	p = query
	tweet_list = authenticate.api.search(q=p+" -RT",count=cnt,lang='en')
	return tweet_list


def analysis(tweet_list):
	positive=negative=neutral=0
	csv_list=[]
	polarity_dict ={}
	for t in tweet_list:
		analyse = TextBlob(t.text)
		j = analyse.sentiment.polarity
		if j > 0:
			positive +=1 
			ex=[clean_tweet(t.text),'1']
			csv_list.append(ex)
			polarity_dict.update({t.text:1})
		elif j==0:
			neutral +=1
			ex=[clean_tweet(t.text),'0']
			csv_list.append(ex)
			polarity_dict.update({t.text:0})
		else:
			negative +=1
			ex=[clean_tweet(t.text),'-1']
			csv_list.append(ex)
			polarity_dict.update({t.text:-1})
	return positive,negative,neutral,csv_list,polarity_dict
