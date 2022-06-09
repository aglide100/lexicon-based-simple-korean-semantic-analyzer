import pandas as pd
from Lexicon import Analyzer
import time

start = time.time()

f = open("./db/text.txt", 'r')
line = f.readline()

dictionary = pd.read_csv('lexicon/polarity.csv')

result = pd.DataFrame({})

while True:
    line = f.readline()
    if not line: break
    
    if len(line) > 3:
        score = Analyzer.analyze_word(line, dictionary)
        if result.empty:
            result = score
        else:
            result = pd.concat([result, score])

    
print(result.describe(include='object'))

print("소요시간 :", time.time() - start) 