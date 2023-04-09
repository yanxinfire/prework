import json
import os
import yaml
from flask import Flask, request
import db

app = Flask(__name__)

configPath = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "config/config.yaml")
with open(configPath) as f:
    cfg = yaml.safe_load(f)

root_api = "/api/v1/prework"
mydb = db.MyDB(cfg)


@app.route(f'{root_api}/users', methods=['GET', 'POST'])
def create_or_list_user():
    if request.method == 'POST':
        return mydb.create_user(request.json)
    if request.method == 'GET':
        start = request.args.get("start", default=0, type=int)
        offset = request.args.get("offset", default=10, type=int)
        first_name = request.args.get("first_name", type=str)
        last_name = request.args.get("last_name", type=str)
        user_data = mydb.get_users(first_name, last_name, start, offset)
        return json.dumps(user_data)


@app.route(f'{root_api}/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def update_or_get_user(user_id):
    if request.method == 'GET':
        return json.dumps(mydb.get_user_by_id(user_id))
    if request.method == 'PUT':
        return mydb.update_user(user_id, request.json)
    if request.method == 'DELETE':
        return mydb.delete_user(user_id)


def main():
    app.run()


if __name__ == '__main__':
    main()
