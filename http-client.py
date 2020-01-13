import requests
import json
#http://www.itwhy.org/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/python/python-%E7%AC%AC%E4%B8%89%E6%96%B9-http-%E5%BA%93-requests-%E5%AD%A6%E4%B9%A0.html
#r = requests.get('http://10.199.96.149:8080/api/v3/banned/?_page=1&_limit=10000',auth=('intelligentFamily-client','Mjg5NTM2NTk1MzI0Mzg2MDExMjg1MDUzODg0NzI1MzI5OTC'))
#print(r.text)
x = "1234567xxx"
r = requests.post(url='http://10.199.96.149:8080/api/v3/banned/',data=json.dumps({
  "who": x,
  "as": "client_id",
  "reason": "banned the clientId",
  "desc": "normal banned",
  "until": 1998377000
}),auth=('intelligentFamily-client','Mjg5NTM2NTk1MzI0Mzg2MDExMjg1MDUzODg0NzI1MzI5OTC'),headers={'Content-Type':'application/json'})
print(r.text)
