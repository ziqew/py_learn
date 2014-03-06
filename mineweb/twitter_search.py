__author__ = 'ziqew'
import const_val
from twitter import *
t = Twitter(auth=OAuth(const_val.TT_OAUTH_TOKEN, const_val.TT_OAUTH_SECRET,
                       const_val.TT_CONSUMER_KEY, const_val.TT_CONSUMER_SECRET))

trends = t.trends.place(_id="1")
print trends
