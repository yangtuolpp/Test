# mocktest
# 2024/4/14
import requests

url = ('http://127.0.0.1:9999/xin')
payload={'key1':'abc','key2':'123'}
res = requests.post(url,params=payload)
print(res.text)


