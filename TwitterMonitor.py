import tweepy
import json
from re import search
from InfoRetriever import InfoRetriever
import time

#insert your twitter app info below
API_KEY =
API_SECRET_KEY = 
ACCESS_TOKEN = 
ACCESS_TOKEN_SECRET = 

#This class receives tweets and filters them
class MaxListner(tweepy.StreamListener):

    def on_data(self, raw_data):

        if self.url_extractor(raw_data) != '':
            url = self.url_extractor(raw_data)

            info_retriever.info_retrieve(url)

            return False
        else:
            return True
#returns error if stream returns a 420
    def on_error(self, status):
        if status == 420:
            return False
#enter in appropriate filters to ensure that tweets come from only the user of interest, this function will 
#extract a url that the user posts and pass that to InfoRetriever
    def url_extractor(self, raw_data):
        key_word = # insert filter information here
        user_id = # insert filter information here
        target_url = ''
        tweet_data = json.loads(raw_data)

        try:
            if search(key_word, tweet_data['text']) and tweet_data['user']['id'] == user_id and not search(
                    'RT @', tweet_data['text']):
                target_url = tweet_data['entities']['urls'][0]['expanded_url']
            else:
                pass
        except:
            pass
        return target_url

#initializes the stream and sets the basic filters provided by twitter api
class MaxStream():

    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self):
        self.stream.filter(follow=[],#enter the twitter id of the user you want to follow as a string in the brackets
                           is_async=True, encoding='utf-8')


if __name__ == '__main__':
    info_retriever = InfoRetriever()
    info_retriever.preload()
    time.sleep(10)

    listener = MaxListner()

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = MaxStream(auth, listener)
    stream.start()
