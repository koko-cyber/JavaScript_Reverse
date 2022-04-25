import requests
import re
import execjs
import json


url = "https://www.cnvd.org.cn/"

session = requests.session()

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
}

session.headers = headers

response = session.get(url)

text = response.text


set_cookie_text = re.findall(r"<script>document.cookie=(.*?);location.href", text)

cookie = execjs.eval(set_cookie_text[0])


cookies = re.split(r'=|;', cookie)

session.cookies.set(cookies[0], cookies[1])

resp = session.get(url=url)

js = resp.text

obj = re.findall(r';go\((.*?)\)', js, re.S)[0]

if 'md5' in obj:
  path = 'D:\\notes\\study\\JS逆向\\JavaScript_Reverse\\JSL\\cookie_md5.js'
elif 'sha1' in obj:
  path = 'D:\\notes\\study\\JS逆向\\JavaScript_Reverse\\JSL\\cookie_sha1.js'
else:
  path = 'D:\\notes\\study\\JS逆向\\JavaScript_Reverse\\JSL\\cookie_sha256.js'

with open(f'{path}', 'r', encoding='utf-8') as f:
    cookie_js = f.read()
    # print(cookie_js)
    ctx = execjs.compile(cookie_js)
    jsl_cookie = ctx.call("cookie", json.loads(obj))

jsl_cookies = re.split(r'=|;', jsl_cookie)

session.cookies.set(jsl_cookies[0], jsl_cookies[1])

res = session.get(url=url)

print(res.text)