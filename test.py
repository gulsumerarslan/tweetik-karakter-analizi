import codecs
import imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import tweepy
import locale
import emoji
import sys
import re
import string
import os



def get_user_tweets(api, username, count=200):
    tweets = api.user_timeline(username, count=count)        
    texts = [tweet.text for tweet in tweets]
    return texts

def get_mentions_names(tweets2):    
    users=[]
    usernamesForTwitter = re.findall( r'(^|[^@\w])@(\w{1,15})\b',tweets2)
    for user in usernamesForTwitter:
        users.append(user[1])    
    return users

def show_html_table(words):
    data = [go.Bar(
            x = words.index.values[:30],
            y = words.values[:30],
            marker= dict(colorscale='Jet',
            color = words.values[:30]),
            text='ranking'
        )]
    layout = go.Layout(
        title='Word Frequency Ranking'
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename=username)    

def show_cloud(listData,typeFormat):    
    a = ' '.join(str(v) for v in listData)  
    wc = WordCloud(background_color="black", max_words=1000, mask=sherlock_mask, stopwords=stopwords)
    wc.generate(a)
    filename=typeFormat+'.png'
    wc.recolor(colormap='PuBu' , random_state=42).to_file(filename)
    #plt.figure(figsize=(80,80))
    #plt.imshow(wc.recolor(colormap='PuBu' , random_state=42),interpolation='bilinear')
    #plt.axis("off")
    #plt.show(block=False)
    
 

def get_tweets():
    #twitter authentication
    CONSUMER_KEY        =  os.getenv('api-key')
    CONSUMER_SECRET     =  os.getenv('api-secret-key')
    ACCESS_TOKEN        =  os.getenv('access-token')
    ACCESS_TOKEN_SECRET =  os.getenv('access-secret-token')
    AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(AUTH)
    return(get_user_tweets(api, username),api.get_user(username).name)

def get_stop_words(listData):
    
    tempStopWord.append("https")
    tempStopWord.append("RT")
    tempStopWord.append("co")
    tempStopWord.append("rt")
    tempStopWord.append("rt'")
    tempStopWord.append("rt '")
    tempStopWord.append("bir")
    tempStopWord.append(",")
    tempStopWord.append(":)")
    tempStopWord.append(":d")

    if not listData:
        return(set(tempStopWord))
    else:
        tempStopWord.extend(listData)
        return(set(tempStopWord))


  
    

def get_clear_data(oldData):
    cevap=0
    rt=0
    tw=0
    lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'Ç'): u'ç',
    ord(u'Ğ'): u'ğ',
    ord(u'Ö'): u'ö',
    ord(u'O'): u'o',
    ord(u'U'): u'u',
    ord(u'Ü'): u'ü',
    ord(u'Ş'): u'ş',
    ord(u'S'): u's',
    }
    tweets=[]
    for data in oldData:
        if data[0] == "@":
            cevap =  cevap + 1
        elif data[0:2] == "RT":
            rt = rt + 1
        else:
            tw = tw + 1
        if data not in stopwords:
            for dataSplit in data.split(" "):            
                if dataSplit not in stopwords:
                    if any(ext in dataSplit for ext in stopwords):
                        tweets.append(dataSplit)  
                              
                    
    datas=[]
    for tweet in tweets:    
        for word in tweet.split(" "):        
            datas.append(emoji.demojize(word.translate(lower_map).lower()))
    if any(ext in "muh" for ext in datas):
        print("url_string")
    return datas
pm = __import__("stop_words")
tempStopWord=list(pm.STOP_WORDS)
image = imageio.imread("sherlock.png")
sherlock_mask = image
args = sys.argv
username = args[1]
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')
stopwords = get_stop_words(None)
name = get_tweets()[1]
train = pd.DataFrame( get_clear_data(get_tweets()[0])) 
words=train.unstack().value_counts()



a = ' '.join(str(v) for v in train.values.tolist())
print(len(a))
show_cloud(train.values.tolist(),"all")
show_cloud(get_mentions_names(a),"users")



userListstopword = ["@" + name for name in get_mentions_names(a)]
get_stop_words(userListstopword)
get_stop_words(get_mentions_names(a))
get_stop_words([ name+" '" for name in get_mentions_names(a)])
stopwords=get_stop_words([ name+"'" for name in get_mentions_names(a)])


train=None
words=None
#with open("out.txt", "w", encoding="utf-8") as f:
    #f.write("$".join(stopwords))

train = pd.DataFrame( get_clear_data(get_tweets()[0])) 
words=train.unstack().value_counts()

show_cloud(train.values.tolist(),"topic")
show_html_table(words)

#with open("outword.txt", "w", encoding="utf-8") as f:
#    f.write('$'.join(str(v) for v in train.values.tolist()))