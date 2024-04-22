import json
import random
import time

import requests


def xhsDetail():

    post_url = 'http://124.223.166.207:80/xhs/xs'

    note_id = '662635ce000000000302233a'

    params = {
        "source_note_id": note_id,
        "image_formats": [
            "jpg",
            "webp",
            "avif"
        ],
        "extra": {"need_body_topic": "1"}
    }

    url = '/api/sns/web/v1/feed'
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

        url = "https://edith.xiaohongshu.com/api/sns/web/v1/feed"
        try:
            payload = json.dumps(params, ensure_ascii=False, separators=(",", ":"))
            response = requests.post(url, data=payload.encode(), headers=headers)
            print(response.text)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    xhsDetail()



