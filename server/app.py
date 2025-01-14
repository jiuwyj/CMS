from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from func import main as r
import json
import time

DEBUG = True

app = Flask(__name__, template_folder="./templates", static_folder="./templates/static")
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

error = '出错啦，请检查输入语句'
data1 = {
    "count": {},
    "data": {},
    "rank": {},
    "truth": {}
}
data2 = {
    "data": {},
    "tree": {},
    "truth_sum": 0.98,
    "datafrom": []
}
data3 = {'validity': 'Yes', 'error': 'error'}


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/datashow', methods=['GET'])
def datashow():
    search = request.values.get('search_val')
    print(search)
    if search == 'city=taipei' or search == "city=Taipei":
        f = open('page2.json', 'r', encoding='utf-8')
        content = f.read()
        dataList = json.loads(content)
        f.close()
        # time.sleep(5)
        return dataList
    else:
        dataList = r.get_page2_data(search)
        return dataList


@app.route('/detail', methods=['GET'])
def detail():
    search = 'ip=' + request.values.get('ip') + ' and port=' + request.values.get('port')
    print(search)

    if search == 'ip=114.32.164.140 and port=80':
        f = open('page3.json', 'r', encoding='utf-8')
        content = f.read()
        detaildata = json.loads(content)
        f.close()
        detaildata["datafrom"] = r.get_ct()
        print(detaildata)
        # time.sleep(5)
        return detaildata
    else:
        detaildata = r.get_page3_data(search)
        return detaildata


@app.route('/check', methods=['GET'])
def check():
    print(request.values.get('search_val'))
    # result = {'validity':'Yes','error':'测试中'}
    result = r.return_grammar_out(request.values.get('search_val'))
    print(result)
    return result


@app.route('/<path:fallback>')
def fallback(fallback):  # Vue Router 的 mode 为 'hash' 时可移除该方法
    if fallback.startswith('css/') or fallback.startswith('js/') \
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
