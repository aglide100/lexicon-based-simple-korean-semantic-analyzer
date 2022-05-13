from Data import Manager
from Lexicon import Analyzer
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

print("Start!")

try:
    file = open("./db/data.db", "rw")
except FileNotFoundError:
    print("File error")
    # raw_data = Manager.get_mock_raw_data()
    # Analyzer.analyze_from_array(raw_data)
except ValueError:
    raw_data = Manager.get_mock_raw_data()

    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
            for sentence in raw_data:
                executor.submit(Analyzer.analyze_word, sentence)



# Manager.create_sqlite()
