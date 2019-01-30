import pymysql
# -*- coding: utf-8 -*-
class Pysql(object):

    def __init__(self, arg):
        self.params = arg
        self.connectSql()


    def connectSql(self):
        self.connection = pymysql.connect(host=self.params['host'],
                             user=self.params['user'],
                             password=self.params['password'],
                             db=self.params['db_name'],
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self.db = self.connection

    def insertData(self, sql):
        # # SQL 插入语句
        # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
        #          LAST_NAME, AGE, SEX, INCOME)
        #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
           # 执行sql语句
           print('进来这里了吗', sql)
           self.cursor.execute(sql)
           # 提交到数据库执行
           self.db.commit()
        except:
           # 如果发生错误则回滚
           self.db.rollback()

    def selectData(self, sql):
        results = []
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 获取所有记录列表
           results = self.cursor.fetchall()
        except:
           print('执行出错')
        return results

    def updateData(self, sql):
        bool = False
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 提交到数据库执行
           self.db.commit()
           on = True
        except:
           # 发生错误时回滚
           self.db.rollback()
        return bool

    def deleteData(self, sql):
        on = False
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
            on = True
        except:
            # 发生错误时回滚
            self.db.rollback()
        return on

    def closeConnect(self):
        self.connection.close()
