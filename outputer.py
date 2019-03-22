# coding: utf-8
import pymysql
class Outputer(object):
    
    def __init__(self):
        # 初始化数据库连接

        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='zscq',
            charset='utf8'
            )

        #self.conn = MySQLdb.Connect(host="localhost", user="root", passwd="MySql123", port=3306)

        self.cursor = self.conn.cursor(); 
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return;
        self.datas.append(data)   # 把数据加入到集合中
    
    # 保存数据到数据库中
    def save_data_todb(self, data):
        # 定义sql语句
        global sql
        global add_data
        sql = """INSERT INTO job_info(type,name,address,salary,public_time,experience,education,company,duty,url)
                VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        add_data = (data['type'], data['name'].encode('utf-8'), data['address'].encode('utf-8'),
               data['salary'].encode('utf-8'), data['public_time'].encode('utf-8'),
               data['experience'].encode('utf-8'), data['education'].encode('utf-8'),
               data['company'].encode('utf-8'), data['duty'].encode('utf-8'), data['url'].encode('utf-8'))
        try:
            self.cursor.execute(sql)# 执行sql数据
            self.conn.commit()  # 提交数据
        except Exception as e:
            print(e)
            self.conn.rollback() # 如果有异常，回滚数据
    # 关闭数据数连接
    def close_db(self):
        self.conn.close()
        self.cursor.close()
    
    # 保存全部数据
    def save_all_data_todb(self):
        # 循环数据数组
        for data in self.datas:

            try:
                self.cursor.execute(sql, add_data) # 执行sql数据
                self.conn.commit() # 提交数据
            except Exception as e:
                print(e)
                self.conn.rollback() # 如果有异常，回滚数据
        self.conn.close() # 关闭数据数连接
        self.cursor.close()
    
    # 输出数据到到output.html
    def output_html(self):
        fout = open('output.html', 'w') #打开output.html文件
        fout.write("<body>") #写入body标签
        fout.write("<table>") #写入table标签
        for data in self.datas: #循环数据数组
            fout.write("<tr>") #写入tr标签
            fout.write("<td>%s</td>" % data['url']) #写入url
            fout.write("<td>%s</td>" % data['type']) #写入type
            fout.write("<td>%s</td>" % data['name'].encode('utf-8')) #写入name
            fout.write("<td>%s</td>" % data['address'].encode('utf-8')) #写入address
            fout.write("<td>%s</td>" % data['salary'].encode('utf-8')) #写入salary
            fout.write("<td>%s</td>" % data['public_time'].encode('utf-8')) #写入public_time
            fout.write("<td>%s</td>" % data['experience'].encode('utf-8')) #写入experience
            fout.write("<td>%s</td>" % data['education'].encode('utf-8')) #写入education
            fout.write("<td>%s</td>" % data['company'].encode('utf-8')) #写入company
            fout.write("<td>%s</td>" % data['duty'].encode('utf-8')) #写入duty
#             fout.write("<td>%s</td>" % data['requirement'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close() # 关闭文件