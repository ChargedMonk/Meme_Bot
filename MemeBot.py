import praw
import urllib
import time
import os.path
import facebook
import random

accesstoken = '*****YourAccessToken*****'


def getimg(x):
    if x == 0:
        all = subreddit.top(limit=15)
    elif x == 1:
        all = subreddit.new(limit=15)
    elif x == 2:
        all = subreddit.rising(limit=15)
    else:
        all = subreddit.hot(limit=15)

    for post in all:
        if post.ups>=250 and (not((str(post.url)) in posturl)):
            if str(post.url).endswith('.jpg'):
                title = str(post.title)
                #print('###### title =', title)
                imgurl = str(post.url)
                #print('****** imgurl =', imgurl)
                posturl.append(imgurl)
                #print('$$$$$$ posturl =', posturl)
                try:
                    response = urllib.request.urlopen(post.url)
                except:
                    break
                img = response.read()

                with open(os.path.join(savepath,'image.jpg'),'wb') as f:
                    f.write(img)
                print('title =', title)
                print('source =', z)
                post_image(title)
                break
        else:
            continue


def post_image(title):
    fb.put_photo(open(img,'rb'),message= (title +'\n(source: /r/'+z+')'))



personalusescript = '************'
secretkey = '*****************'
useragent = 'YourUserAgent'
user = 'UserName'
userpass = '***password***'

reddit = praw.Reddit(client_id=personalusescript, client_secret=secretkey, user_agent=useragent, username=user, password=userpass)

savepath = 'F:/BotZenos/'
img = 'image.jpg'

subs = ['dankmemes','edgymemes','adviceanimals','me_irl', '4ChanMeta', 'ClopClop', 'destiny', 'cuckold', 'IndianpeopleFacebook', 'unexpectedjihad', 'fakehistoryporn', 'nottheonion','MeanJokes']

z=''
posturl = list()
c=0

while True:
    print('c =',c)
    z=random.choice(subs)
    subreddit = reddit.subreddit(z)
    getimg(random.randint(0,4))
    time.sleep(10)
    #print(time.time())
    c+=1
    if c>48:
        c=0
        posturl.clear()
