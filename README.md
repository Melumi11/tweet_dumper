# tweet_dumper
Download (all) past tweets from a twitter user

To use, you have to create a Twitter developer account and create a project. Install tweepy (pip), and put your twitter dev API key, secret, access token, secret, and bearer token at the top of the tweet_dumper.py file.

Specify the user who you want to download tweets from and how many tweets you want downloaded. Tweets are downloaded in order of latest.

You can set the increment to download 5-100 tweets at a time, so if save_number = 121 and increment = 100, it will download 200 tweets.

I set it to exclude replies and retweets by your person but you can change that if you wish.

Currently the output consists of columns "id", "created_at" (ISO 8601), "likes", "replies", "retweets", "url", "text"

Only twitter essential access is required. It's easy to upload the outputed csv to google sheets or something. If it downloads but doesn't output try cding into the directory or in vscode opening the folder that tweet_dumper.py is in.

I used some code from yanofsky (https://gist.github.com/yanofsky/5436496) and Jan Kirenz (https://www.kirenz.com/post/2021-12-10-twitter-api-v2-tweepy-and-pandas-in-python/twitter-api-v2-tweepy-and-pandas-in-python/) but I couldn't find what I want to do specifically so I made it myself
