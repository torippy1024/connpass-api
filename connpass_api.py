import requests
import sys
import datetime
from datetime import date
import json

def get_connpass_json(ymd: date, count: int = 100, order: int = 2):
    url = "https://connpass.com/api/v1/event/"
    url += "?ymd="+ymd.isoformat().replace("-", "")+"&count="+str(count)+"&order="+str(order)
    print(url)

    response = requests.get(url)
    json_data = response.json()

    return json_data


def main():
    ymd = date.today()
    if len(sys.argv) > 1 and is_num(sys.argv[1]):
        ymd += datetime.timedelta(days=float(sys.argv[1]))

    json_data = get_connpass_json(ymd)
    with open('build/today.json', 'w', encoding="UTF-8") as f:
        json.dump(json_data, f, ensure_ascii=False)    


def is_num(s) -> bool:
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    main()