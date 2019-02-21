import json
import requests
import os

os.system('rm /etc/proxychains.conf')
os.system('cp /etc/proxychains.conf.bak /etc/proxychains.conf')
filename = "/etc/proxychains.conf"
url = "http://39.105.2.91:8899/api/v1/proxies"
res = requests.get(url = url)
shuju = json.loads(res.text)
for i in shuju['proxies']:
    if shuju['is_valid'] 
    with open(filename, 'a+') as f:
        if i['is_https'] == "true":
            f.write("https"+shuju['ip']+" "+shuju['port'])
