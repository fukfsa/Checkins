import requests
import os

COOKIE = os.environ["COOKIE"]

def main():
    rs = requests.get("https://appapis.dmall.com/static/userIsCheckIn.jsonp?callback=jQuery22304504064425163671_1582705578650&venderId=1&_=1582705578651",
                      headers={
                          "Host":"api.m.mi.com",
                          "Device-id":"ffffffff-dc56-1bac-9c1c-96300033c587",
                          "Cookie":f"{COOKIE}",
                          "Network-Stat":"4G",
                          "Network-Carrier":"46002",
                          "Mishop-Cilent-Id":"180100031052",
                          "Accept-Encoding":"gzip",
                          "Mishop-Client-VersionCode":"20210302",
                          "Mishop-Auth":"7cd64608118f2ab4;3306177275",
                          "Screen-height-px":"1560",
                          "Ai-Recommend-Status":"1",
                          "Mishop-Model":"HLK-AL00",
                          "Uuid":"d05069e9-218e-eeb6-04cd-42baad25f249",
                          "Screen-DensityDpi":"320",
                          "Mishop-Is-Pad":"0",
                          "device":"P8Abbqf8TC1yddYrRFOIxQ==",
                          "Android-Ver":"29",
                          "Connect-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                          "Connect-Length":"91",
                          "Connection":"Keep-Alive"
                            }
                         )    
                        
    print(rs)
    print(rs.headers)
    print('-'*30)
    print("Text",rs.text)
    pass


if __name__ == "__main__":
    main()
    pass
