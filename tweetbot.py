from os import access
import openai, tweepy, random, accessapi

def bot():
    client = tweepy.Client(consumer_key = accessapi.api_key, consumer_secret= accessapi.api_key_secret, access_token = accessapi.access_token, access_token_secret =accessapi.access_token_secret)
    openai.api_key = accessapi.openai_api_key

    response = openai.Completion.create(
        engine = "text-davinci-001",
        prompt = "A poem on mental health",
        max_tokens = 64
    )
    text = response.choices[0].text + "\n \n #mentalhealth #poems"
    print(text)
    reply_y_or_n= input("Shall I print the tweet?")
    if reply_y_or_n == 'y':
        tweet = client.create_tweet(text = text)
        print(tweet)
        print("Tweet successful!")
    else:
#       print("else works")
        bot()

if __name__ == "__main__":
    bot()