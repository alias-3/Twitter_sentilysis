import tweepy
from textblob import TextBlob
from . import authenticate


def tweets(query,cnt=20):
	p = query
	tweet_list = authenticate.api.search(q=p+" -RT",count=cnt)
	return tweet_list
def analysis(tweet_list):
	positive=negative=neutral=0
	pos_dict=neg_dict=net_dict={}
	for t in tweet_list:
		analyse = TextBlob(t.text)
		j = analyse.sentiment.polarity
		if j > 0:
			positive +=1 

		elif j==0:
			neutral +=1

		else:
			negative +=1

	return positive,negative,neutral
