import requests
import yaml

root_api = "/api/v1/prework"

def list_user(args):
    url = f"http://{args.host}:{args.port}{root_api}/users?1=1"
    if args.first_name is not None:
        url += f"&first_name={args.first_name}"
    if args.last_name is not None:
        url += f"&last_name={args.last_name}"
    if args.start >= 0:
        url += f"&start={args.start}"
    if args.offset >= 0:
        url += f"&offset={args.offset}"
    res = requests.get(url)
    return res.json()


def create_user(args):
    with open(args.user_file, 'r') as f:
        data = yaml.safe_load(f)
    res = requests.post(f"http://{args.host}:{args.port}{root_api}/users", json=data)
    return res.json()["msg"] if "msg" in res.json() else res.json()["error"]
