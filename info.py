from wxpy import *
import datetime
from pysql import Pysql as ySql

db = ySql({
        "host": "localhost",
        "user": "root",
        "password": "123456",
        "db_name": "kz-front"
     })

def insertData(params):
    print('开始插入数据')
    sql = "INSERT INTO article(nick_name, title, url, time) VALUES ('{nick_name}', '{title}', '{url}', '{time}')".format(nick_name=params['nick_name'], title=params["title"], url=params["url"], time=params["time"])
    db.insertData(sql)

def main():
    bot = Bot(cache_path=True, console_qr=True)
    allGroup = bot.groups()
    # 定位群
    company_group = ensure_one(allGroup.search('筷子前端2018【没高层群】'))
    print('开始接收信息-------')
    # 将消息转发到文件传输助手
    @bot.register(company_group, except_self=False)
    def forward_boss_message(msg):
        # print(msg.member)
        # print(msg.sender)
        # print(msg.raw)
        # print(msg.articles)
        # print('asdfasdf----', str(msg))
        # print('Sharing' in str(msg))
        originData = msg.raw
        if 'Sharing' in str(msg):
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {
              "nick_name": originData['ActualNickName'],
              "title": originData['Text'],
              "url": originData['Url'],
              "time": str(time),
            }
            insertData(data)
            msg.forward(bot.file_helper, prefix=time)
        else:
            print()
    # 堵塞线程
    bot.join()

main()
