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

username = "wendys" # person who you're downloading
save_number = 100 # the number of tweets you want to download
alltweets = [] # don't touch

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
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = client.get_users_tweets(id = id,
									exclude = ["retweets,replies"],
									tweet_fields=['created_at'],
										max_results=100)

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
										tweet_fields=['created_at'],
											max_results=100,
											end_time = oldest)
			
			#save most recent tweets
			alltweets.extend(new_tweets.json()['data'])
			
			#update the time of the oldest tweet less one

			oldest = alltweets[-1].get("created_at")
			
			print(f"...{len(alltweets)} tweets downloaded so far")
	except Exception: traceback.print_exc()

	outtweets = [[tweet.get("id"), tweet.get("created_at"), tweet.get("text")] for tweet in alltweets]

	#write the csv  
	with open('tweets_output.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass

get_all_tweets()