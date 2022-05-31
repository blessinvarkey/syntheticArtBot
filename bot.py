from urllib import response
import tweepy

#API_KEY = ''
#API_SECRET = ''
#ACCESS_TOKEN = ''
#SECRET_ACCESS_TOKEN = ''
#BEARER_TOKEN = ''


client = tweepy.Client(consumer_key =API_KEY, consumer_secret= API_SECRET, access_token = ACCESS_TOKEN, access_token_secret =SECRET_ACCESS_TOKEN)
response = client.create_tweet(text="Hello World!")
print(response)
#client = tweepy.Client(bearer_token= BEARER_TOKEN)
#query = "GauGAN"
#response = client.search_recent_tweets(query=query)
#print(response)
#for tweet in response.data:
#    print(tweet.id)
