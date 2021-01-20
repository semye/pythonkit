# 连接mysql数据库

import pymysql

if __name__ == "__main__":
    conn = pymysql.connect(user='root', password='', database='semye', charset='utf8')
    print(conn)
    conn.close()
