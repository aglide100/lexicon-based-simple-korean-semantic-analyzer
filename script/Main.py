from Data import Manager
from Lexicon import Analyzer
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
import time
import pandas as pd

print("Start!")
start = time.time()
# try:
#     file = open("./db/data.db", "rw")
# except FileNotFoundError:
#     print("File error")
#     # raw_data = Manager.get_mock_raw_data()
#     # Analyzer.analyze_from_array(raw_data)
# except ValueError:
data = pd.read_csv("./db/data.csv", sep="\t")


if __name__ == "__main__":
    dictionary = pd.read_csv('lexicon/polarity.csv')
    
    for idx, row in data.itertuples():
        Analyzer.analyze_word(row, dictionary)


#raw_data = Manager.get_mock_raw_data()
#for sentence in raw_data:
#    Analyzer.analyze_word(sentence)


print("소요시간 :", time.time() - start) 
    # if __name__ == "__main__":
    #     with ProcessPoolExecutor(max_workers=1) as executor:
    #         for sentence in raw_data:
    #             executor.submit(Analyzer.analyze_word, sentence)

# Manager.create_sqlite()
