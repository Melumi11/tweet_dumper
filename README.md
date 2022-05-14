# tweet_dumper
Download (all) past tweets from a twitter user

To use, you have to create a Twitter developer account and create a project. Install tweepy (pip), and put your twitter dev API key, secret, access token, secret, and bearer token at the top of the file.

Specify the user who you want to download tweets from and how many tweets you want downloaded. Tweets are downloaded in order of latest.

I set it to exclude replies and retweets and output tweet id, date/time of tweet, and tweet contents but you can change that if you wish.

Only essential access is required.

I used some code from yanofsky (https://gist.github.com/yanofsky/5436496) and Jan Kirenz (https://www.kirenz.com/post/2021-12-10-twitter-api-v2-tweepy-and-pandas-in-python/twitter-api-v2-tweepy-and-pandas-in-python/) but I couldn't find what I want to do specifically so I made it myself
