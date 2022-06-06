#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import requests
import traceback

#Twitter API credentials
consumer_key = "" # API key
consumer_secret = "" # API key secret
access_key = "" # Access token
access_secret = "" # Access token secret
bearer_token = ""

username = "youtube" # person who you're downloading (ex. youtube or wendys)
save_number = 400 # the number of tweets you want to download
increment = 100 # between 5 and 100 - how many to download at a time
# if save_number is not divisible by increment, it will download the closest multiple of increment above save_number
# ex. if save_number = 121 and increment = 100, it will download 200 tweets

alltweets = [] # don't touch this

def get_all_tweets():
	#Twitter only allows access to a users most recent 3240 tweets with this method (I got this number from elsewhere, I'm not 100% sure)

	#authorize twitter, initialize tweepy
	client = tweepy.Client(bearer_token = bearer_token, 
							consumer_key = consumer_key,
							consumer_secret = consumer_secret,
							access_token = access_key,
							access_token_secret = access_secret,
							return_type = requests.Response,
							wait_on_rate_limit=True)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []  
	id = client.get_user(username=username).json()['data'].get("id")
	#make initial request for most recent tweets (200 is the maximum allowed count [I think it's actually 100])
	new_tweets = client.get_users_tweets(id = id,
									exclude = ["retweets,replies"],
									tweet_fields=['created_at,public_metrics'],
										max_results=increment)

	#save most recent tweets
	alltweets.extend(new_tweets.json()['data'])
	#save the time of the oldest tweet less one
	oldest = alltweets[-1].get("created_at")

	#keep grabbing tweets until there are no tweets left to grab (or it hits your max)
	try:
		while len(alltweets) < save_number:
			print(f"getting tweets before {oldest}")
			
			#all subsiquent requests use the end_time param to prevent duplicates
			new_tweets = client.get_users_tweets(id = id, 
										exclude = ["retweets,replies"],
										tweet_fields=['created_at', 'public_metrics'],
											max_results=increment,
											end_time = oldest)
			
			#save most recent tweets
			alltweets.extend(new_tweets.json()['data'])
			
			#update the time of the oldest tweet

			oldest = alltweets[-1].get("created_at")
			
			print(f"...{len(alltweets)} tweets downloaded so far")
	except Exception: traceback.print_exc()

	outtweets = [[tweet.get("id"), tweet.get("created_at"), tweet.get("public_metrics").get("like_count"), tweet.get("public_metrics").get("reply_count"), tweet.get("public_metrics").get("retweet_count"), "https://twitter.com/twitter/statuses/" + tweet.get("id"), tweet.get("text")] for tweet in alltweets]

	#write the csv  
	with open('tweets_output.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at", "likes", "replies", "retweets", "url", "text"])
		writer.writerows(outtweets)

	pass

get_all_tweets()
