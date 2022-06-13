import psycopg2

class Databases():
    def __init__(self, host, dbname, user, password, port):
        self.db = psycopg2.connect(host=host, dbname=dbname,user=user,password=password,port=port)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

class CRUD(Databases):
    def insertDB(self, schema, table, colum, data):
        sql = "INSERT INTO {schema}.{table}({colum}) VALUES ('{data}') ;".format(schema=schema,table=table,colum=colum,data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" insert DB err ",e) 
    
    def readDB(self, schema, table, colum):
        sql = "SELECT {colum} FROM {schema}.{table}".format(colum=colum, schema=schema, table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = ("read DB err : ", e)
        
        return result

    def readTextFromArticleInJob(self, colum, id):
        # sql = "SELECT (\"Content\", \"Id\") FROM article WHERE \"" + colum + "\" = '" + id + "'"
        sql = "SELECT * FROM article WHERE \"" + colum + "\" = '" + id + "'"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = ("Read DB err : ", e)

        return result

    def updateScore(self, Score_pos, Score_neg, Score_neut, Score_comp, Score_none, Score_max_value, Score_max_name, Id):
        sql = ("UPDATE \"article\"" 
        " SET "
        " \"Score_pos\" "
        " = '{Score_pos}',"
        " \"Score_neg\" "
        " = '{Score_neg}',"
        " \"Score_neut\" "
        " = '{Score_neut}',"
        " \"Score_comp\" "
        " = '{Score_comp}',"
        " \"Score_none\" "
        " = '{Score_none}',"
        " \"Score_max_value\" "
        " = '{Score_max_value}',"
        " \"Score_max_name\" "
        " = '{Score_max_name}'"
        " WHERE "
        " \"Worker_id\""
        " = '{Id}'"
        ).format(Score_neg = Score_neg, Score_pos = Score_pos, Score_neut = Score_neut, Score_comp = Score_comp, Score_none = Score_none, Score_max_value = Score_max_value, Score_max_name = Score_max_name, Id = Id)
        
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err : ", e)

    def updateDB(self, schema, table, colum, value, condition):
        sql = "UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(schema=schema
        , table=table , colum=colum, value=value, condition=condition)
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("update DB err : ", e)

    def deleteDB(self, schema, table, condition):
        sql = "DELETE FROM {schema}.{table} WHERE {condition}".format(schema=schema,table=table,
        condition=condition)
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err : ", e)