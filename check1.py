import requests
import json
import os
from bs4 import BeautifulSoup

# PUSH_KEY = os.environ["PUSH_KEY"]
COOKIE = os.environ["COOKIE"]


def login():
    url = "http://api.m.mi.com/v1/scoresign/sign_check_in"
    headers = {
        "Host":"api.m.mi.com",
        "Device-id":"ffffffff-dc56-1bac-9c1c-96300033c587",
        "Cookie":f"{COOKIE}",
        "Network-Stat":"4G",
        "Network-Carrier":"46002",
        "Mishop-Cilent-Id":"180100031052",
        "Accept-Encoding":"gzip",
        "Mishop-Client-VersionCode":"",
        "Mishop-Auth":"",
        "Screen-height-px":"1560",
        "Ai-Recommend-Status":"1",
        "Mishop-Model":"HLK-AL00",
        "Uuid":"",
        "Screen-DensityDpi":"320",
        "Mishop-Is-Pad":"0",
        "device":"P8Abbqf8TC1yddYrRFOIxQ==",
        "Android-Ver":"29",
        "Connect-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Connect-Length":"91",
        "User-Agent":"okhttp/3.12.3",
        "Connection":"Keep-Alive",
        "timestamp_mishop_client":"1617407798892",
        "nonce_mishop_client":"e1a020be4c1acdcb7904e83eb6320361"
    }

   
    res = requests.post(url=url, headers=headers)

if __name__ == '__main__':
    main()
    pass
