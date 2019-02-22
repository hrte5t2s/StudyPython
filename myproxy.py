import json
import requests
import os

os.system('rm /etc/proxychains.conf')
os.system('cp /etc/proxychains.conf.bak /etc/proxychains.conf')
filename = "/etc/proxychains.conf"
url = "#######################"
res = requests.get(url = url)
shuju = json.loads(res.text)
for i in shuju['proxies']:
    if shuju['is_valid']:
        with open(filename, 'a+') as f:
            if i['is_https']:
                f.write("https "+shuju['ip']+" "+str(shuju['port']))
            else:
                f.write("http "+shuju['ip']+" "+str(shuju['port']))
    else:
        continue
