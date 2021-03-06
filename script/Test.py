import pandas as pd
from Lexicon import Analyzer
import time

#data = pd.read_csv("./db/data.csv", sep="\t")
start = time.time()

dataSet = pd.read_csv("./db/movie_review.csv")

data = dataSet.drop(["score"], axis=1)
# scores = dataSet.drop(["text"], axis=1)
dictionary = pd.read_csv('lexicon/polarity.csv')

result = pd.DataFrame({})

for idx, row in data.itertuples():
    score = Analyzer.analyze_word(row, dictionary)
    if result.empty:
        result = score
    else:
        result = pd.concat([result, score], axis = 0)
    # insert_to_frame = pd.DataFrame(data=score)
    # result.append(score, ignore_index=True)

success = 0
fail = 0

result = pd.merge(result, dataSet, how='left')

# result = result.reset_index(drop=True)
for index, row in result.iterrows():
    if row['max'] == "None":
        continue

    if row['max'] == "COMP":
        continue

    if row['max'] == "NEUT":
        continue

    if row['max'] == "POS":
        if row['score'] == 1:
            success += 1
        else:
            print("-------------")
            print("it should be NEG")
            print(row['text'])
            print(row['pos'], row['neg'])
            print("   ")
            fail +=1
    elif row['max'] == "NEG":
        if row['score'] == 0:
            success += 1
        else:
            print("-------------")
            print("it should be POS")
            print(row['text'])
            print(row['pos'], row['neg'])
            print("   ")
            fail +=1

print("correct", success)
print("fail", fail)

print("소요시간 :", time.time() - start) 