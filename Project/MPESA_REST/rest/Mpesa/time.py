from datetime import date, datetime
import types

import urllib3
import json

http= urllib3.PoolManager()

def mpesa_time():
    # now=datetime.now()

    # year=now.strftime("%Y")
    # month=now.strftime("%m")
    # date=now.strftime("%d")
    # hour =int(now.strftime("%H"))
    # min=now.strftime("%M")
    # sec=now.strftime("%S")

    res=http.request(method='GET',url="http://worldtimeapi.org/api/timezone/Africa/Nairobi")
    data=json.loads(res.data.decode('utf-8'))
    # return f"{year}{month}{date}{hour}{min}{sec}"
    # year=string(data['datetime'])[0,3]
    # print(year)
    print(type(data['datetime']))
    t=str(data['datetime'])
    year=t[0:4]
    month=t[5:7]
    date=t[8:10]
    hour=t[11:13]
    min=t[14:16]
    sec=t[17:19]

    return f"{year}{month}{date}{hour}{min}{sec}"