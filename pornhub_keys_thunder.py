from bs4 import BeautifulSoup as bs
import requests,re,os,sys
from lxml import etree
import js2py
from lxml import etree
from tqdm import tqdm
import subprocess
import base64




thunder_path = r'I:\thunder\Program\Thunder.exe'

def Url2Thunder(url):
    url = 'AA' + url + 'ZZ'
    url = base64.b64encode(url.encode('ascii'))
    url = b'thunder://' + url
    thunder_url = url.decode()
    return thunder_url
 
 
def download_with_thunder(file_url):
    thunder_url = Url2Thunder(file_url)
    subprocess.call([thunder_path, thunder_url])

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
    'Referer':'https://www.pornhub.com/'}


def keywords_url(keys,num):
    print('正在获取页面...')
    url = 'https://www.pornhub.com/video/search?search='+keys
    r = requests.get(url,headers=headers)
    html = r.content
    dom = etree.HTML(html)
    urls = dom.xpath('//a[contains(@href,"viewkey")]/@href')
    rurls = []
    for i in urls[::2]:
        rurl = 'https://www.pornhub.com'+i
        rurls.append(rurl)
    
    if num:
        return rurls[5:num+5]

    return rurls[5:]

#解密js
def exeJs(js):
    flashvars = re.findall('flashvars_\d+', js)[0]
    res = js2py.eval_js(js + flashvars)
    if res.quality_720p:
        return res.quality_720p
    elif res.quality_480p:
        return res.quality_480p
    elif res.quality_240p:
        return res.quality_240p



def download(rurls,address,key):
    print("正在解析页面..")
    for url in rurls:   
        headers_1={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
            'Referer':url}
        r = requests.get(url,headers=headers_1)
        html = etree.HTML(r.content)
        
       
        title=re.findall(r'<span class="inlineFree">(.*?)</span>',str(r.content,errors='ignore'))
        js_temp = html.xpath('//script/text()')
        for j in js_temp:
            if 'flashvars' in j:
                js = ''.join(j.split('\n')[:-8])

                #URL
                videoUrl = exeJs(js)

                download_with_thunder(videoUrl)              
if __name__ == "__main__":

    key = '***'
    
    #path
    address = 'H://pornhub/'
    
    # file number
    num = 3
    
    key_urls = keywords_url(key,num)
    download(key_urls,address,key)
