
from email.mime import base
import json
import base64

def mpesa_password(paybill,passKey,m_time):
    en=paybill+passKey+m_time

    encoded=base64.b64encode(en.encode())
    return encoded.decode('ascii')