import API_CONFIG
import time
from TwitterAPI import TwitterAPI
from datetime import date, timedelta, datetime
from operator import itemgetter



######
YESTERDAY = date.today() - timedelta(1)
YESTERDAY = YESTERDAY.strftime('%m%d%y')
######


class TwitterDaily:

    def __init__(self):
        consumer_secret = API_CONFIG.CONSUMER_SECRET
        access_token_secret = API_CONFIG.ACCESS_TOKEN_SECRET
        access_token_key = API_CONFIG.ACCESS_TOKEN_KEY
        consumer_key = API_CONFIG.CONSUMER_KEY
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def format_date(self, date):
        return datetime.strptime(date, '%a %b %d %X %z %Y').strftime('%m%d%y')

    def not_yesterday(self, last_avail_data):
        if YESTERDAY != last_avail_data:
            return True

    def tweet_popularity(self, tweet):
        *_, total_fav, total_retweet = tweet
        return total_fav+total_retweet

    def tweet_dimensions(self, tweet):
        popularity = self.tweet_popularity(tweet)
        name, text, *_ = tweet
        return [name, text, popularity]

    def format_tweet_string(self, tweet):
        name, tweet, popularity = tweet
        statement = "{0} tweeted {1}. The tweet had a popularity of {2}.".format(name, tweet, popularity)
        return statement

    def yesterday_tweets(self, user_tweets):
        yesterday_tweets = []
        for tweet in user_tweets:
            last_avail_date = self.format_date(tweet['created_at'])

            # The date is sorted... if Tweets are not from yesterday, we break from the loop
            if self.not_yesterday(last_avail_date):
                break
            yesterday_tweets.append([tweet['user']['name'], tweet['text'], tweet['favorite_count'], tweet['retweet_count']])
        return yesterday_tweets

    def tweet_info(self):
        tweets_dict = {}
        sorted_tweets = self.sorted_tweets()

        for i, tweet in enumerate(sorted_tweets):
            tweet_string = self.format_tweet_string(tweet)
            tweets_dict[i+1] = tweet_string

        return tweets_dict

    def sorted_tweets(self, top_n=5):
        tweets = self.tweets_list()

        # Sorted the tweets from high to low based on its popularity
        tweet_list = sorted(tweets, key=itemgetter(2), reverse=True)
        return tweet_list[:top_n]

    def total_followers(self):
        return list(id for id in self.api.request('followers/ids'))

    def total_following(self):
        return list(id for id in self.api.request('friends/ids'))

    def twitter_circle(self):
        followers = self.total_followers()
        following = self.total_following()
        return [following, followers]

    def tweets_list(self):
        following, followers = self.twitter_circle()
        all_tweets = []

        for ids in following:
            tweets = self.api.request('statuses/user_timeline', {'user_id': ids})
            try:
                user_tweets = tweets.json() if tweets.status_code == 200 else 'PROBLEM: ' + tweets.text # Will need to change for yesterday and not last tweet
                tweets_found = self.yesterday_tweets(user_tweets)
                if tweets_found:
                    for tweet in tweets_found:
                        name, text, popularity = self.tweet_dimensions(tweet)
                        all_tweets.append([name, text, popularity])

            except (IndexError, TypeError):
                pass

        return all_tweets

    @staticmethod
    def upload_yesterday():
        twitter = TwitterDaily()
        return twitter.tweet_info()
