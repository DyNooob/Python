#!/usr/bin/python
import pandas
import csv, sqlite3
conn= sqlite3.connect('chat_log.db')
# 新建数据库为 chat_log.db
df = pandas.read_csv('chat_logs.csv', sep=",")
# 读取我们上一步提取出来的csv文件，这里要改成你自己的文件名
df.to_sql('my_chat', conn, if_exists='append', index=False)
# 存入my_chat表中
 
conn = sqlite3.connect('chat_log.db') 
# 连接数据库
cursor = conn.cursor()
# 获得游标
cursor.execute('select content from my_chat where length(content)<30') 
# 将content长度限定30以下，因为content中有时候会有微信发过来的东西
value=cursor.fetchall()
# fetchall返回筛选结果
 
data=open("聊天记录.txt",'w+',encoding='utf-8') 
for i in value:
    data.write(i[0]+'\n')
# 将筛选结果写入 聊天记录.txt
 
data.close()
cursor.close()
conn.close()
# 关闭连接