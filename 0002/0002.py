#!/usr/bin/env python
import  pymysql,random,string

create_table_sql=""" create table secret_keys(
                        keyss int,valuess char(30))"""

insert_table_sql="""insert into secret_keys(keyss,valuess)
                    values('{keyss}','{valuess}')"""

def activation_code(count,length):
    base=string.ascii_letters+string.digits
    return [''.join(random.sample(base,length)) for i in range(count)]

def insertintomydb(data):
    db=pymysql.connect('127.0.0.1','root','123456','test')

    try:
        with db.cursor() as cursor:
            cursor.execute(create_table_sql)
            db.commit()
            
            i=0
            for values in data :
                cursor.execute(insert_table_sql.format(keyss=i,valuess=values))
                i=i+1
            db.commit()
    except:
            db.close()
            print('插入失败！')
    
if __name__ == '__main__':
    data= activation_code(200,20)
    insertintomydb(data)
