# 已经封装好mysql类了，就不用导入pymsql了，直接导入封装好的类

from readMysql import Mysqldb

# 实例化
my_db = Mysqldb()

# 写查询SQL语句
sql = "select * from case_file where id<5"
# 查询所有
select_all = my_db.select_all(sql)
print("查询所有数据：\n", select_all)
# 查询一条
select_one = my_db.select_one(sql)
print("查询一条数据：\n", select_one)
# 查询多条
select_many = my_db.select_many(sql, 3)
print("查询3条数据：\n", select_many)

# 新增一条数据
name=None
value = (f'{name}','null','9999','','','','')
sql = f"insert into case_file values {value}"
insert_one = my_db.commit_data(sql)
# 新增多条数据
values = "('aaa',null), (18, 'bbb'), (19, 'ccc')"
sql = f"insert into case_file ( `case_name`, `path`) values {values}"
insert_many = my_db.commit_data(sql)

# 修改数据
sql = "update case_file set case_name = '出不去了' where id = 17"
my_db.commit_data(sql)

# 删除数据
sql = "delete from case_file where id = 17"
my_db.commit_data(sql)

#--------------------------*************************-----------------

def where_condition(whereInfo:dict):
    '''
    拼接where条件
    @whereInfo where条件
    '''
    sql = ""
    whereConditionList = whereInfo.keys()
    if(len(whereConditionList)>0):
        sql = " where"
        for column in whereConditionList:
            sql += " "+column+"=\""+whereInfo[column]+"\""
            sql += " and"
        sql=sql[:-3]
    return sql


def gen_insert_sql(tableName, columnInfo:dict):
    '''
    生成insert的sql语句
    @tableName，插入记录的表名
    @columnInfo,插入的数据，字典
    '''
    #字段列表
    sequnceList = columnInfo.keys()
    sql = 'insert into %s (' % tableName
    for column in sequnceList:
        sql += "'"+column+"',"
    sql = sql[:-1]
    sql += ") values ("
    for column in sequnceList:
        sql += "\""+columnInfo[column]+"\","
    sql = sql[:-1]+");"
    return sql

def gen_update_sql(tableName,updateInfo:dict,whereInfo:dict):
    '''
    生成update的sql语句
    @updateInfo，更新的记录信息
    @whereInfo,条件信息
    '''
    sequnceList = updateInfo.keys()
    sql="update %s set " % tableName
    for column in sequnceList:
        sql+=column+"=\""+str(updateInfo[column])+"\","
    sql = sql[:-1]
    sql += where_condition(whereInfo)
    sql += ";"
    return sql

#生成查询sql
def gen_single_select_sql(tableName,columnList:list,whereInfo:dict):
    '''
    生成select的sql语句
    @tableName 查询的表名
    @columnList 查询的列名集合
    @whereInfo,条件信息
    '''
    sql="select "
    if(len(columnList)>0):
        sql += ','.join(str(column) for column in columnList)
    else:
        sql += "*"
    sql += " from %s " % tableName
    sql += where_condition(whereInfo)
    sql += ";"
    return sql

def gen_delete_sql(tableName,whereInfo:dict):
    '''
    生成select的sql语句
    @tableName 查询的表名
    @columnList 查询的列名集合
    @whereInfo,条件信息
    '''
    sql = "delete %s " % tableName
    sql += where_condition(whereInfo)
    sql += ";"
    return sql




