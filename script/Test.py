from Data import Manager
from Lexicon import Analyzer
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
import pandas as pd

import time

print("Start!")
start = time.time()

data = pd.read_csv("./db/data.csv", sep="\t")

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
        # analyzer = Analyzer()
        for idx, row in data.itertuples():
            executor.submit(Analyzer.analyze_word, row)



print("소요시간 :", time.time() - start) 
# Manager.create_sqlite()
