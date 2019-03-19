import pymysql

def connection():
    conn = pymysql.connect(host="localhost",user="root",passwd="vampires2010",db="demo")
    c = conn.cursor()
    return c, conn