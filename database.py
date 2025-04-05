import requests
import pymysql
import json
import time
# 目标数据库配置
target_db_config = {
    "host": "rm-2ze84ic0r024iuwuf4o.mysql.rds.aliyuncs.com",
    "port": 3306,
    "user": "haohan",
    "password": "Haohanblue233",
    "connect_timeout": 36000,
    "database": "datawander",
}

def execute_sql(sql_query):
    target_db_config = {
        "host": "rm-2ze84ic0r024iuwuf4o.mysql.rds.aliyuncs.com",
        "port": 3306,
        "user": "haohan",
        "password": "Haohanblue233",
        "database": "datawander",
        "connect_timeout": 36000,
    }
    try:
        # 连接到目标数据库
        connection = pymysql.connect(
            host=target_db_config["host"],
            port=target_db_config["port"],
            user=target_db_config["user"],
            database=target_db_config["database"],
            password=target_db_config["password"],
            connect_timeout=target_db_config["connect_timeout"],
        )

        # 创建游标
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # 执行SQL查询
            cursor.execute(sql_query)
            # 获取查询结果
            result = cursor.fetchall()
            print(result)
            # 返回结果
            return result

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 确保连接关闭
        if connection:
            connection.close()

schema =[
{
    "description":"全国的景区数据",
    "table_name":"all_cite",
    "fields":[{'Field': '景区名', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '等级', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '所属省', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '地址', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '评定时', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '发布时', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '发布链', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'lng_GCJ02', 'Type': 'float', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'lat_GCJ02', 'Type': 'float', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'lng_BD09', 'Type': 'float', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'lat_BD09', 'Type': 'float', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'lng_WGS84', 'Type': 'float', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'lat_WGS84', 'Type': 'float', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '所属城', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '所属区', 'Type': 'varchar(254)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
},
{
    "description":"景点数据",
    "table_name":"cite_data",
    "fields":[{'Field': 'province', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'name', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'level', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'comment', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'price', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'volume', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'address', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'location', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'short', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'free', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'strictLocation', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'video', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
},
{
    "description":"景区评论",
    "table_name":"comment_cite",
    "fields":[{'Field': '名称', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '英文名', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'id', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'poiID', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '经度', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '维度', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': ' 标签', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '特色', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '价格', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '最低价 格', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '评价分数', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '评论数量', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': ' 封面图片', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '成人票价格', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '老人票价格', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '学生票价格', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '儿童票价格', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '建议游玩', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '开放时间', 'Type': 'varchar(3000)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '介绍', 'Type': 'varchar(5000)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': '优待政策', 'Type': 'varchar(3000)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
},
{
    "description":"评论详情",
    "table_name":"comment_detail",
    "fields":[{'Field': 'ID', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'comment', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
},
{
    "description":"各地的美食数据",
    "table_name":"food_data",
    "fields":[{'Field': 'province', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'city', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'name', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'introduce', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'url', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'img_urls', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
},
{
    "description":"景区数据表",
    "table_name":"tourism_data",
    "fields":[{'Field': 'id', 'Type': 'bigint', 'Null': 'YES', 'Key': 'MUL', 'Default': None, 'Extra': ''}, {'Field': 'name_zh', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'score', 'Type': 'double', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'comment_num', 'Type': 'bigint', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'home_page_comment', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'ranking', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'name_en', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'Introduction', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'address', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'opening_time', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'phone', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'website', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'arrival_method', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'tickets', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'update_time', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'provence', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
},{
    "description":"网站的用户数据表",
    "table_name":"user_data",
    "fields":[{'Field': 'account', 'Type': 'varchar(255)', 'Null': 'NO', 'Key': 'PRI', 'Default': None, 'Extra': ''}, {'Field': 'password', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'usertype', 'Type': 'varchar(255)', 'Null': 'NO', 'Key': 'PRI', 'Default': None, 'Extra': ''}, {'Field': 'phone', 'Type': 'varchar(255)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
}
]



if __name__ == '__main__':
    table_name = "mf_dividend"
    sql = f"describe user_data;"
    result = execute_sql(sql)
    # print(json.dumps(result, indent=4, ensure_ascii=False))