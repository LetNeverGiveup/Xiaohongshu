import json
import random
import time

import requests


def get_search_id():
    e = int(time.time() * 1000) << 64
    t = int(random.uniform(0, 2147483646))
    return base36encode((e + t)).lower()


def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, int):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


def xhsSearch():

    post_url = 'http://124.223.166.207:80/xhs/xs'

    keywords = '上海'
    search_id = get_search_id()

    params = {
        "keyword": keywords,
        "page": 1,
        "page_size": 20,
        "search_id": search_id,
        "sort": "general",
        "note_type": 0,
        "ext_flags": [],
        "image_formats": [
            "jpg",
            "webp",
            "avif"
        ]
    }
    url = '/api/sns/web/v1/search/notes'
    a1 = ''  # Cookie会中的a1参数
    web_session = ""  # Cookie会中的web_session参数

    data = {
        "url": url,
        "params": json.dumps(params, ensure_ascii=False, separators=(",", ":")),
        "a1": a1
    }

    response = requests.post(post_url, data=json.dumps(data))

    if response.status_code == 200:
        json_data = json.loads(response.text)

        headers = {
            "accept": "application/json, text/plain, */*",
            "cache-control": "no-cache",
            "content-type": "application/json;charset=UTF-8",
            "cookie": f"a1={a1}; web_session={web_session};",
            "origin": "https://www.xiaohongshu.com",
            "referer": "https://www.xiaohongshu.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            'X-S': json_data['X-s'],
            'X-T': str(json_data['X-t'])
        }

        url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
        try:
            payload = json.dumps(params, ensure_ascii=False, separators=(",", ":"))
            response = requests.post(url, data=payload.encode(), headers=headers)
            print(response.text)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    xhsSearch()
