#!/bin/env python3

from flask import Flask, request
import sys,os
import json
import random
from skpy import Skype


# Slype Setting

sk_user  = 'bot account'
sk_pass  = 'bot login pass'
sk_group = 'chat group'


app = Flask(__name__)

base_path  = os.path.dirname(os.path.abspath(__file__))
image_dir  = os.path.join(base_path , 'images')


@app.route('/knowledge_webhock',methods=['POST'])
def knowledge_webhock():

    logfile = os.path.join(base_path,'create.log')
    if not os.path.isfile(logfile) :
        f = open(logfile, "w")
        f.write("")
        f.close()

    if request.method == 'POST':    
        data = request.data
        str = data.decode('utf-8').replace("'", '"')
        body = json.loads(str)
        
        if body["status"] == "created" :
            date  = body["insert_date"]
            user  = body["insert_user"]
            title = body["title"]
            link  = body["link"] 

            message = '''
{user} さんが新規投稿しました！
Title : {title}
URL   : {url}
'''.format(user=user , title=title, url=link)

            sk = Skype(sk_user, sk_pass)
            for c in sk.chats.recent():
                chat = sk.chats[c]
                if hasattr(chat, 'topic') and chat.topic == sk_group :
        
        
                    chat.sendMsg(message)
        
                    file_name = random.choice(os.listdir(image_dir))
                    img_file  = os.path.join(image_dir , file_name)
                    
                    chat.sendFile(open(img_file, 'rb'), '_' , image=True)
        
                
                    break
    return ""


if __name__ == "__main__":
    app.run()
