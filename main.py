from flask import Flask
import requests

app = Flask(__name__)

# --- Costom Vision API のプロジェクトを作成 ---


def get_pets_data():
    # url = f"{os.environ.get('EndPoint')}customvision/v3.3/Training/projects?name=testcv002"
    url = "https://sheets.googleapis.com/v4/spreadsheets/1fIePGDbSQ80xQrK6QwWfb5EPQKtl1pcTgtfiQSs0knE/values/pets?key=AIzaSyCwIfAOPR1euxoN-7_UcbMIjRSWzwH3IIo"
    response = requests.get(url)
    return response

# --- Costom Vision API のプロジェクトを作成 ---


def get_health_checkup_data():
    # url = f"{os.environ.get('EndPoint')}customvision/v3.3/Training/projects?name=testcv002"
    url = "https://sheets.googleapis.com/v4/spreadsheets/1fIePGDbSQ80xQrK6QwWfb5EPQKtl1pcTgtfiQSs0knE/values/健康診断?key=AIzaSyCwIfAOPR1euxoN-7_UcbMIjRSWzwH3IIo"
    response = requests.get(url)
    return response


@app.route("/")
def helloworld():
    return "<p>Hello world</p>"


@app.route("/output")
def goutput_data():
    # データ取得
    pets_r = get_pets_data().json()
    health_checkup_r = get_health_checkup_data().json()
    # データの整形(pets)
    keys01 = pets_r["values"][0]
    values01 = pets_r["values"][1:]
    results01 = [dict(zip(keys01, item)) for item in values01]

    # データ成形(health_checkup)
    keys02 = health_checkup_r["values"][0]
    values02 = health_checkup_r["values"][1:]
    results02 = [dict(zip(keys02, item)) for item in values02]

    # PetIDを軸にしてDictを結合
    for i in results01:
      petid = i["PetID"]
      # ❓petIDはnumber型でいいのか❓今はいけてる
      include_id_list = list(filter(lambda item : item['PetID'] == petid, results02))
      i["helth"] = include_id_list[0:]

    # 辞書型から指定した値を持つものをデータを取得
    # print(list(filter(lambda item : item['name'] == 'Taro', results)))
    return results01


@app.route("/ou")
def goutp_data():
    health_checkup_r = get_health_checkup_data().json()
    keys = health_checkup_r["values"][0]
    values = health_checkup_r["values"][1:]
    results = [dict(zip(keys, item)) for item in values]
    return results
