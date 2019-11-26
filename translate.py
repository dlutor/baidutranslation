import requests
import os
import re
import execjs
os.environ["EXECJS_RUNTIME"] = "Node"
class trans(object):
    def __init__(self):
        proxies = {'http': None, 'https': None}
        headers = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                   }
        self.proxies = proxies
        self.headers = headers

        self.s = requests.session()
        self.get_token()
        self.token, self.gtk = self.get_token()
        self.raw_js = self.read('transl.js', 'r')


    def get(self,url):
        return self.s.get(url=url,headers=self.headers,proxies=self.proxies)#,timeout=1
    def post(self, url, data):
        return self.s.post(url=url, headers=self.headers, proxies=self.proxies, data=data)
    def read(self,path,mode):
        with open(path,mode) as f:
            data=f.read()
        return data
    def get_token(self):
        url='https://fanyi.baidu.com/'
        r=self.get(url)
        pattern="token: '(.*?)',"
        result=re.findall(pattern,r.text)[0]
        gtk_pattern="window.gtk = '(.*?)';"
        gtk=re.findall(gtk_pattern,r.text)[0]
        return result,gtk
    def get_sign(self,p,l):
        js=execjs.compile(self.raw_js)
        a=js.call('main',p,l)
        return a
    def transl_entozh(self,p):
        sign=self.get_sign(p,self.gtk)
        data={
            'from':'en',
            'to':'zh',
            'query':p,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign':sign,
            'token':self.token
        }
        url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        r=self.post(url,data)
        return r.json()

    def main(self):
        print('输入一段文本,例如:Python is the best program lanugue in the word!\n')
        p='Python is the best programing language in the word!'
        result=self.transl_entozh(p)
        print('结果：'+result['trans_result']['data'][0]['dst'])
        while True:
            p=input('输入一段文本\n')
            result=self.transl_entozh(p)
            print('结果：'+result['trans_result']['data'][0]['dst'])






if __name__ == '__main__':
    t=trans()
    t.main()