import requests
import yaml

root_api = "/api/v1/prework"
headers = {"Host": "prework.yx.com"}


def list_user(args):
    output = '|{:<4s}|{:<12s}|{:<12s}|{:<3s}|\n'.format('id', 'first_name', "last_name", "age")
    output += '-' * 36 + '\n'
    url = f"http://{args.host}:{args.port}{root_api}/users?1=1"
    if args.first_name is not None:
        url += f"&first_name={args.first_name}"
    if args.last_name is not None:
        url += f"&last_name={args.last_name}"
    if args.start >= 0:
        url += f"&start={args.start}"
    if args.offset >= 0:
        url += f"&offset={args.offset}"
    res = requests.get(url, headers=headers)
    for u in res.json():
        output += '|{:<4d}|{:<12s}|{:<12s}|{:<3d}|\n'. \
            format(u["id"], u["first_name"], u["last_name"], u["age"])
    return output


def get_user(args):
    url = f"http://{args.host}:{args.port}{root_api}/user/{args.user_id}"
    res = requests.get(url, headers=headers)
    u = res.json()
    return '{:<12s}: {}\n{:<12s}: {}\n{:<12s}: {}\n{:<12s}: {}\n'. \
        format("id", u["id"], "first_name", u["first_name"],
               "last_name", u["last_name"], "age", u["age"])


def create_user(args):
    with open(args.user_file, 'r') as f:
        data = yaml.safe_load(f)
    res = requests.post(
        f"http://{args.host}:{args.port}{root_api}/users",
        headers=headers,
        json=data
    )
    return res.json()["msg"] if "msg" in res.json() else res.json()["error"]


def update_user(args):
    with open(args.user_file, 'r') as f:
        data = yaml.safe_load(f)
    res = requests.put(
        f"http://{args.host}:{args.port}{root_api}/user/{args.user_id}",
        headers=headers,
        json=data
    )
    return res.json()["msg"] if "msg" in res.json() else res.json()["error"]


def delete_user(args):
    res = requests.delete(
        f"http://{args.host}:{args.port}{root_api}/user/{args.user_id}",
        headers=headers
    )
    return res.json()["msg"] if "msg" in res.json() else res.json()["error"]
