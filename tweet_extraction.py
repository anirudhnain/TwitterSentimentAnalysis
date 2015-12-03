from slistener import SListener
import time, tweepy, sys

# #Consumer Keys and access tokens, used for OAuth
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def main():
    track = ['southpaw','black mass','blackmass','maze runner','mazerunner']
 
    listen = SListener(api, 'movie_data')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track, languages=["en"])
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()