#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://node-31.zeno.fm/4g65yz9gg0quv.aac?rj-ttl=5&rj-tok=AAABdtuvkw4A9ORsR7htLe8_1Q")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '709294532')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '1062262'))
    CHAT = int(os.environ.get("CHAT", "-1001215436654"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "YQLVRM-TYUGMT-YXPFEJ-QWYZWQ-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "842fe1d408d10364f90ec785a533feaf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1914403790:AAFBfFSp7sldc8E1SqfjbApkrcFlk0NiQt8") 
    SESSION = os.environ.get("SESSION_STRING", "BQCtOF_k9zTRLc95bbq2rwe_RV816F5wCZisGJZ_bh-0x_h1053fBhot6ISBR5O_yOfkr5nWQkhAqv89wyW_9ofbcHOdqNx01CzgpjXsk7NsE8-pjo15OUXKPAXoSXFggWYxKHhZ6Ziuxh-mAulehTwwfO-Zuwf0KTM1s934QT6f4XgeoEhpLqoTHZ0-SlYMqf7pi18AM2-Xij5nOErcobB2CT2WWt50qD58zpsNVGlXwl2WYwDRqz3HWusVtO4jfwgK7oElzit6d1fSgzrLuKVvDwxLZzfDu8pl9jIx8jmkfD-CI83Udb6YD5BLL07Q3oj4VIEEX8jOqQAoXOTer9gTKkb5xAA")
    playlist=[]
    msg = {}
