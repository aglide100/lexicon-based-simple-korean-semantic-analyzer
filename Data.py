import sqlite3

class Manager:
    def get_mock_raw_data():

        raw_data = []

        content4 = "이것좀보세요 https://github.com/FLAIST/emosent-py"
        content2 = "기아우승 확신 100% 😂"
        content3 = "부상부위도 특이하네"
        content6 = "1💜🔥💜🔥🤩 ☂ 👰‍♂️ 🧟‍♂️ 🧍‍♀️ 🤦‍♂️ 🙇‍♀️ 🧎‍♂️ 🫀 🥵 👺 🧑‍🏫 👩‍🎨"
        # 🤩
        content5 = "어린이날입니다 아이돌 여러분들은 이날만을 위해 묵혀둔 과거사진을 준비해주시고 소속사에서는 n년전 비하인드영상을 풀어주시기 바랍니다 아무것도없으면 정신을좀차리시길바랍니다"
        content = "어린이날🫶🏻🍓🌱"
        # raw_data.append(title)

        raw_data.append(content)
        raw_data.append(content2)
        raw_data.append(content3)
        raw_data.append(content4)
        raw_data.append(content5)
        raw_data.append(content6)
        
        # raw_data.extend(comments)

        return raw_data
    def get_from_csv():

        raw_data = []

        return raw_data

    def create_sqlite():
        conn = sqlite3.connect("./db/data.db")

        cur = conn.cursor()

        conn.execute('CREATE TABLE data(postID TEXT, content TEXT, postedDate TEXT)')

        # cur.executemany()

        conn.commit()
        conn.close()

        return