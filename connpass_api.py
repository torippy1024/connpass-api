import requests
import sys
from datetime import date, datetime, timezone, timedelta
import json

def get_connpass_json(ymd: str, count: int = 100, order: int = 2):
    url = "https://connpass.com/api/v1/event/"
    url += "?ymd="+ymd+"&count="+str(count)+"&order="+str(order)
    print(url)

    response = requests.get(url)
    json_data = response.json()
    print(type(json_data))

    return json_data


def main():
    JST = timezone(timedelta(hours=+9))
    ymd = datetime.now(JST)
    if len(sys.argv) > 1 and is_num(sys.argv[1]):
        ymd += timedelta(days=float(sys.argv[1]))
    ymd_str = ymd.isoformat().split("T")[0].replace("-", "")

    json_data = get_connpass_json(ymd_str)
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