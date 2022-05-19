from Data import Manager
from Lexicon import Analyzer
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
import pandas as pd

import time

print("cpu_count: ", mp.cpu_count())
start = time.time()

data = pd.read_csv("./db/data.csv", sep="\t")

analyzer = Analyzer()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
        
        for idx, row in data.itertuples():
            executor.submit(analyzer.analyze_word, row)



print("소요시간 :", time.time() - start) 
# Manager.create_sqlite()
