from Data import Manager
from Lexicon import Analyzer
from concurrent.futures import ProcessPoolExecutor
#from multiprocessing import Process, shared_memory, Semaphore
import multiprocessing as mp
import pandas as pd
from konlpy.tag import Kkma
import time
#import os


print("cpu_count: ", mp.cpu_count())
start = time.time()

data = pd.read_csv("./db/data.csv", sep="\t")

#for idx, row in data.itertuples():
#   Analyzer.analyze_word(row, dictionary, m)

if __name__ == "__main__":
    dictionary = pd.read_csv('lexicon/polarity.csv')
    
    with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:   
        for idx, row in data.itertuples():
            executor.submit(Analyzer.analyze_word, row, dictionary)
        


print("소요시간 :", time.time() - start) 
# Manager.create_sqlite()
