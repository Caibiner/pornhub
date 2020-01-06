from bs4 import BeautifulSoup as bs
import requests,re,os,urllib,sys
from threading import Thread

def download_mp4(url,dir,headers):
    req=requests.get(url=url,headers=headers)
    filename=str(dir)+'/1.mp4'
    with open(filename,'wb') as f:
        f.write(req.content)


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
    'Referer':'https://www.pornhub.com'}
  
if __name__ == "__main__":
    page = 1
    path =''
    ts = []
    while page<1000:
        print("第%d段"%page)
        #视频的URL放下行(Request URL)，注意 str(page)改成下列形式
        url ='https://cv-h.phncdn.com/hls/videos/202001/04/273838141/,720P_4000K,480P_2000K,240P_400K,_273838141.mp4.urlset/seg-'+str(page)+'-f2-v1-a1.ts?tW7RbMgafU3rBHX9Ratevjho3bYwS3cks6Lp30gmti8uS6x6Mhqhmeig02xYK2kdziqiUsJqzcIg-xmHTuws-AYRjOTQ7po-q4TpQfyyHZH9ocwEfTTDvqmJVtq-SLEbrDP5hfg4tTcEpceKDE7NRJDJLFx8V8qDlVEGfdBL1s6GvFdxjQ'
        r = requests.get(url,headers=headers)
        if r.status_code !=200:
            break
        with open (path+'%d.mp4'%page,'ab') as f:
            f.write(r.content)
            f.close()
    
