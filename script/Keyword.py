import os
import grpc
import psycopg2
import Database
import pandas as pd
from Lexicon import Analyzer

import manager_pb2
import manager_pb2_grpc

# host = "localhost"
# dbname = "keyword"
# user = "table_admin"
# password = "HelloWorld"
# port = "8432"


dictionary = pd.read_csv('lexicon/polarity.csv')

host = os.environ['DB_ADDR']
dbname = os.environ['DB_NAME']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
port = os.environ['DB_PORT']
worerId = os.environ['WORKER_ID']

def callGRPCDone():
    with grpc.insecure_channel("keyword_manager:50010") as channel:

        client = manager_pb2_grpc.ManagerStub(channel)
        response = client.DoneAnalyzer(manager_pb2.DoneAnalyzerReq(id=worerId))
        print(response)

try:
    db = Database.Databases(host, dbname, user, password, port)
except psycopg2.DatabaseError as db_err:
    print(db_err)

if __name__ == '__main__':
    # result = Database.CRUD.readTextFromArticleInJob(db, 'Job_id', 'test')
    result = Database.CRUD.readTextFromArticleInJob(db, 'Worker_id', worerId)

    for value in result:
        print(value[0])
        score = Analyzer.analyze_word(value[0], dictionary)
        Database.CRUD.updateScore(db, score['pos'].values[0], score['neg'].values[0], score['neut'].values[0], score['comp'].values[0], score['none'].values[0], score['max'].name, score[score['max'].name].values[0], value[13])

    callGRPCDone()

