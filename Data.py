import sqlite3

class Manager:
    def get_mock_raw_data():

        raw_data = []

        # ! 분석 불가 문장
        # content = "하하 호호"
        # content2 = "문장이 아니면 문제가 생기는듯"
        # content3 = "집에 가고 싶다"
        content4 = "1💜🔥💜🔥🤩 ☂ 👰‍♂️ 🧟‍♂️ 🧍‍♀️ 🤦‍♂️ 🙇‍♀️ 🧎‍♂️ 🫀 🥵 👺 🧑‍🏫 👩‍🎨"
        # 🤩
        # content5 = "어린이날입니다 아이돌 여러분들은 이날만을 위해 묵혀둔 과거사진을 준비해주시고 소속사에서는 n년전 비하인드영상을 풀어주시기 바랍니다 아무것도없으면 정신을좀차리시길바랍니다"
        # content6 = "어린이날🫶🏻🍓🌱"
        # raw_data.append(title)

        # raw_data.append(content)
        # raw_data.append(content2)
        # raw_data.append(content3)
        raw_data.append(content4)
        # raw_data.append(content5)
        # raw_data.append(content6)
        
        # raw_data.extend(comments)

        return raw_data
    def get_from_csv():

        raw_data = []

        return raw_data

    def create_sqlite():
        conn = sqlite3.connect("./db/data.db")

        cur = conn.cursor()

        # cur.executemany()

        conn.commit()
        conn.close()

        return