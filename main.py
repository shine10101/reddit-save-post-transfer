import praw
import codecs
from bs4 import BeautifulSoup

reddit = praw.Reddit(client_id="",
                    client_secret="",
                    user_agent="",
                    username="",
                    password="")

savedposts = "reddit_export.html"
sp = codecs.open(savedposts, "r", "utf-8")
soupy = BeautifulSoup(sp, 'html.parser')

for link in soupy.find_all('a'):
    l = link.get('href')
    id = l.split('/')[-3]
    if l.startswith('https://www.reddit.com'):
        try:
            sub = reddit.submission(id=id)
            sub.save(category="view later")
            print(id)
        except:
            print("Submission ID", id, "not saved")

