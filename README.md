# Transfer all saved posts from one reddit account to another (simple | fast method)

# Getting Started

## Download saved posts

Step 1: Open any browser and go to the following URL: [https://redditmanager.onrender.com/app#](https://redditmanager.onrender.com/app#)

Step 2: Connect RedditManager to original (old) reddit account containing saved posts

Step 3: Export all items. The result should be a **reddit_export.html** file

## Create Reddit Script/bot

Step 4: Sign in to Reddit using new account details

Step 5: Create Reddit Script: 

- Go to https://www.reddit.com/prefs/apps
- Give any name and description.
- Select 'script'
- Redirect uri: http://localhost:8080
- Press "create app"
- Make note of **client id** (text below "web app"), and **secret**.

## Save posts to new Reddit account

Step 6. Open main.py file and enter the following details:
- client_id="" # Client ID
- client_secret="" # Client secret
- user_agent="" # Reddit app name
- username="" # Reddit(new) username
- password="" # Reddit(new) password

Step 6: Run main.py