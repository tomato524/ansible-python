from flask import Flask, make_response ,request
import subprocess
from waitress import serve
import sys

# import json
api = Flask(__name__)

#yamlファイルを生成
@api.route('/create', methods=['GET'])
def create():
    print('/createにアクセスがありました。')
    ip = request.args.get('ip')
    subprocess.run(['python','convert.py',ip],shell=True)
    print('yamlファイルが生成しました。')
    return make_response('yamlファイルを作成しました。')

#ansibleの実行
@api.route('/ansible', methods=['GET'])
def ansible():
    print('/ansibleにアクセスがありました。')
    #subprocess.run(['ansible','convert.py'],shell=True)
    print('ansibleを実行しました。')
    return make_response('ansibleを実行しました。')

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=3000)