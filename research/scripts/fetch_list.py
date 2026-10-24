# -*- coding: utf-8 -*-
"""拉取 B 站用户视频列表（wbi 签名版），输出 JSON。"""
import json
import time
import urllib.request
from hashlib import md5
from urllib.parse import urlencode

MID = 523945494
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Chrome/120.0)",
      "Referer": "https://space.bilibili.com/"}

MIXIN_KEY_ENC_TAB = [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
                     33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
                     61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
                     36, 20, 34, 44, 52]


def get_wbi_keys():
    url = "https://api.bilibili.com/x/web-interface/nav"
    req = urllib.request.Request(url, headers=UA)
    data = json.load(urllib.request.urlopen(req, timeout=20))["data"]["wbi_img"]
    img = data["img_url"].rsplit("/", 1)[1].split(".")[0]
    sub = data["sub_url"].rsplit("/", 1)[1].split(".")[0]
    raw = img + sub
    return "".join(raw[i] for i in MIXIN_KEY_ENC_TAB)[:32]


def wbi_sign(params, key):
    params = dict(sorted(params.items()))
    params["wts"] = int(time.time())
    qs = urlencode(params)
    params["w_rid"] = md5((qs + key).encode()).hexdigest()
    return params


def fetch_page(page, key):
    base = "https://api.bilibili.com/x/space/wbi/arc/search"
    p = {"mid": MID, "pn": page, "ps": 30, "tid": 0, "order": "pubdate", "platform": "web"}
    url = base + "?" + urlencode(wbi_sign(p, key))
    req = urllib.request.Request(url, headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=20))


def main():
    key = get_wbi_keys()
    all_v = []
    page = 1
    while True:
        d = fetch_page(page, key)
        if d.get("code") != 0:
            print("API error:", d.get("code"), d.get("message"))
            break
        vlist = d["data"]["list"]["vlist"]
        if not vlist:
            break
        all_v.extend(vlist)
        pages = d["data"]["page"]["count"] // d["data"]["page"]["ps"] + 1
        print(f"page {page}/{pages}: {len(vlist)} videos (total {len(all_v)})")
        if page >= pages:
            break
        page += 1
        time.sleep(1.2)
    with open("bili_videos.json", "w", encoding="utf-8") as f:
        json.dump(all_v, f, ensure_ascii=False, indent=1)
    print("saved", len(all_v), "videos -> bili_videos.json")
    for v in all_v:
        print(v["created"], v["bvid"], f"{v['length']:>8}", v["title"])


if __name__ == "__main__":
    main()
