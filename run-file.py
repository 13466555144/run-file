# -*-coding:utf-8 -*-
def file_qc():
    import json
    import requests
    with open("access20200107.log", "rb") as file:
        while 1:
            lines = file.readlines() #带缓存读取
            dict1={}#定义字典存储clienid和树目的映射关系
            line_num = 0
            if not lines:
                break
            for line in lines:
                line_num = line_num+1
                #print (type(line))   #打印读取类型<class 'bytes'>
                line2 = bytes.decode(line) #byte转<class 'str'>
                #print('读取内容line2:',line2)
                line3 = line2.replace("escape=json","")
                #print('处理数据line3:',line3)
                #jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
                jsonLine = json.loads(line3)#格式化成json对象
                dm = jsonLine["dm"]
                #print('处理line3中dm值:',dm)#读取json对象中dm字段的值
                dm_num = 0
                if dm in dict1:#判断字典中是否已经存在值
                    dm_num = dict1[dm]
                    dm_num = dm_num+1
                dict1[dm]=dm_num
                #print('相同DM值数量统计',dict1)#相同DM值数量统计
            #print('相同DM值数量统计',dict1)#相同DM值数量统计
            # s = set()
            print('文件遍历结束，开始遍历字典筛选符合条件clientid，最终字典长度：',len (dict1))
            s = []
            for key in dict1:
                num = dict1[key]
                if num > 50: #重复超过15次的就加入黑名单
                    print(key+':'+str(dict1[key]))
                    v = key.split('&')
                    #print('v:'+str(v))  #打印v列表
                    vs = v[0].replace("clientid=","")#截取出最终的clientid
                    r = requests.post(url='http://10.199.96.149:8080/api/v3/banned/',data=json.dumps({"who": vs,"as": "client_id","reason": "banned the clientId","desc": "normal banned","until": 1998377000}),auth=('intelligentFamily-client','Mjg5NTM2NTk1MzI0Mzg2MDExMjg1MDUzODg0NzI1MzI5OTC'),headers={'Content-Type':'application/json'})
                    print('加入emqx黑名单成功clientid:',vs)
                    s.append(vs)
            print('筛选最终符合条件clientid数量：',len (s))
            #将字典值写到文件中
            str_dict1 = str(s)#转换成字符串
            f = open('dict1.txt','w')#当前目录创建一个可写文件
            f.writelines(str_dict1)
            f.close() #关闭文件
            
if __name__=="__main__":
    file_qc()
