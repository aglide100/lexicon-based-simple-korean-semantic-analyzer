import os
import psycopg2
import Database
import pandas as pd
from Lexicon import Analyzer

host = os.environ['DB_ADDR']
dbname = os.environ['DB_NAME']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
port = os.environ['DB_PORT']
worerId = os.environ['WORKER_ID']
# host = "localhost"
# dbname = "keyword"
# user = "table_admin"
# password = "HelloWorld"
# port = "8432"


dictionary = pd.read_csv('lexicon/polarity.csv')

try:
    db = Database.Databases(host, dbname, user, password, port)
except psycopg2.DatabaseError as db_err:
    print(db_err)

# result = Database.CRUD.readTextFromArticleInJob(db, 'Job_id', 'test')
result = Database.CRUD.readTextFromArticleInJob(db, 'Worker_id', worerId)

for value in result:
    print(value[0])
    score = Analyzer.analyze_word(value[0], dictionary)
    Database.CRUD.updateScore(db, score['pos'].values[0], score['neg'].values[0], score['neut'].values[0], score['comp'].values[0], score['none'].values[0], score['max'].name, score[score['max'].name].values[0], value[13])
