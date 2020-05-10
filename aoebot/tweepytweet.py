import tweepy
import time
auth = tweepy.OAuthHandler('*************',
                           '*******************')
auth.set_access_token(
    '-*****************', '***************')

api = tweepy.API(auth)

user = api.me()
# print(user.followers_count)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    # if follower.followers_count >100 :
    # print(follower.name)
    # follower.follow()

search_string = 'voobly'
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        # tweet.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
