# import twitter
#
#
#
# api=twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_secret)
#
# print (api.verifyCredentials())

import tweepy

consumer_key="REf4WjS1J9xKEMcjPKGdo1MJT"
consumer_secret="LmbacJYnMnaDHfGCjSf6AlaLZnOv8cUKUYBhngbRMSSsxKc0ec"
access_token="175046594-rlc2LODoFs9ZBV4XQvY0iDo8syP5pRGKBgI7cqrS"
access_secret="n5QPwUhny5BNWBEtwgnaHHo1YHFrxyiVfLKUT6AMywAg7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search=api.search(q="music",rpp=10)
print (search)