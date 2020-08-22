# -*- coding: utf-8 -*-

import battlenet
from battlenet import Connection

if __name__ == "__main__":
    
    connection = Connection(public_key='7a09ed83ea0740e0bf284e903c8a029f', private_key='6HNxhgBdt92TrO7bUFj0bByKWywOzAtw', locale='cn')
    realms = connection.get_all_realms(battlenet.CHINA)
    print(realms)

    # import hmac

    # secret_key1 = b'This is my secret key'
    # message1 = b'Hello world'
    # hex_res1 = hmac.new(secret_key1, message1, digestmod="MD5").hexdigest()
    # print(hex_res1)  # b8908a20bd70f465330b434e18441d3b