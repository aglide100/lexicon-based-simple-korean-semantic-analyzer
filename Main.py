from Data import Manager
from Lexicon import Analyzer



try:
    file = open("./db/data.db", "rw")
except FileNotFoundError:
    print("File error")
    # raw_data = Manager.get_mock_raw_data()
    # Analyzer.analyze_from_array(raw_data)
except ValueError:
    raw_data = Manager.get_mock_raw_data()
    Analyzer.analyze_from_array(raw_data)


# Manager.create_sqlite()
