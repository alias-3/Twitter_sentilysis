import tweepy


consumer_key = 'jn9wVMNXUnmcQc7JFwPaspR34'
consumer_secret_key = 'vEvA42j6H4W8mB1faQWnC7vcaRGXuQe3kxd4kMQBu1Raupd93t' 

access_token = '1058315016905068546-ztrnkxZ6VRM7j40CRnDWe6i8UIc3Ev'
access_token_secret = 'Tk6hEKhBdO5aDwztZRK0p7HYnibvoqJvTfGVtucwoqtfV' 

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)