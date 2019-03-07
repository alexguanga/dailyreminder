# -*- coding: utf-8 -*-


# TODO: Work on improving the way the information is printed
import email
import smtplib
import API_CONFIG
import itertools
from datetime import date, timedelta, datetime
from PodcastDaily import PodcastDaily
from FitnessPalDaily import FitnessPalDaily
from TwitterDaily import TwitterDaily
import email.message
import email_html

######
YESTERDAY = date.today() - timedelta(1)
YESTERDAY = YESTERDAY.strftime('%m%d%y')
######


class EmailDaily:
    def __init__(self):
        self.FROM = API_CONFIG.EMAIL_ADDRESS
        self.TO = API_CONFIG.EMAIL_ADDRESS
        self.username = API_CONFIG.EMAIL_ADDRESS
        self.password = API_CONFIG.EMAIL_PASSWORD

    def send_message(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        msg = email.message.Message()
        msg['From'] = self.FROM
        msg['To'] = self.TO

        subject = self.write_subject()
        msg['Subject'] = subject

        email_content = self.write_html_body()

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)

        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.close()

    def write_html_body(self):
        twitter_info = CreateEmailBody.body_message_twitter()
        fitness_info = CreateEmailBody.body_message_fitness()
        podcast_info = CreateEmailBody.body_message_podcast()

        email_body = email_html.email_content(twitter_info, podcast_info, fitness_info)
        return email_body

    def write_subject(self):
        return  "Daily Journal for {0}".format(YESTERDAY)

class CreateEmailBody:
    @staticmethod
    def remove_unicde(string):
        return ''.join([i if ord(i) < 128 else ' ' for i in string])

    @staticmethod
    def body_message_podcast():
        podcast_open_statement = "The following are the podcast you heard on {0}: \n".format(YESTERDAY)
        podcast_content = PodcastDaily.upload_yesterday()
        podcast_content = list(itertools.chain.from_iterable(podcast_content.values()))
        podcast_content = [podcast_info + "<br/>" for podcast_info in podcast_content]
        podcast_string = ', '.join(podcast_content)
        podcast_string = CreateEmailBody.remove_unicde(podcast_string)
        podcast_all_content = '\n'.join([podcast_open_statement, podcast_string])
        return podcast_all_content

    @staticmethod
    def body_message_fitness():
        fitness_dict = FitnessPalDaily.upload_yesterday()
        fitness_meals = fitness_dict.values()
        fitness_meals = list(itertools.chain.from_iterable(fitness_meals))
        fitness_meals = [meal + "<br/>" for meal in fitness_meals]
        return('\n'.join(fitness_meals))

    @staticmethod
    def body_message_twitter():
        tweets_dict = TwitterDaily.upload_yesterday()
        tweets_position = tweets_dict.keys()
        tweets_content = tweets_dict.values()

        tweets_format_update = []
        for pos, tweet in zip(tweets_position, tweets_content):
            statement = "Tweet Rank {0}: {1}".format(pos, tweet)
            statement = CreateEmailBody.remove_unicde(statement)
            statement = "- " + statement + "<br/>"
            tweets_format_update.append(statement)

        tweets_format_update = '\n'.join(tweets_format_update)
        return tweets_format_update
