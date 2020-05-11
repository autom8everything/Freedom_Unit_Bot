#!/usr/bin/env python3

import praw, threading,time
import csvreader as csvr
import subreddit_patroller as patrol


def run_bot():
    #read credentials
    with open(".credentials") as c:
        bot_client_id = c.readline().strip()
        bot_client_secret = c.readline().strip()
        bot_username = c.readline().strip()
        bot_password = c.readline().strip()
        bot_agent = c.readline().strip()
        
    
    #reddit API login
    bot = praw.Reddit(client_id=bot_client_id,
                      client_secret=bot_client_secret,
                      username=bot_username,
                      password=bot_password,
                      user_agent=bot_agent)
                      
    print(f"client_id={bot_client_id}\nclient_secret={bot_client_secret}\nusername={bot_username}\npassword={bot_password}\nuser_agent={bot_agent}")
    
    #subreddits to target
    subreddits = ["theydidthemath","LearnPython"]
    patrol_sub = [True, True]
    frequency = [3,1] #comment on one in every x comments
    
    
    #configuring what to target
    keyphrase = "!FreedomUnitsBot" #bot name
    
    #reading in CSV file
    units = csvr.csv2dict("unit_conversions.csv")
    
    #creating thread instances
    bot_threads = []
    for subname,shouldpatrol,freq in zip(subreddits,patrol_sub,frequency):
        bot_threads.append(threading.Thread(target=patrol.patrol,
            args=(bot,units,subname,keyphrase,shouldpatrol,freq)))

        
    #starting threads
    for cthread in bot_threads:
        cthread.start()
        
    #letting execute
    while True:
        time.sleep(1)
        
        
if __name__ == "__main__":
    run_bot()