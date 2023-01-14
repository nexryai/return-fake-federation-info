import json
import random

import falcon


def randstr(length):
    return ''.join([chr(random.randint(97, 122)) for _ in range(length)])

def randtld():
    i = random.randint(0, 3)
    if i == 0:
        return ".com"
    elif i == 1:
        return ".org"
    elif i == 2:
        return ".net"
    elif i == 3:
        return ".one"

class return_fake:
    def on_post(self, req, resp):
        dict = []

        for i in range (1,500):
            dict.append({"isSuspended": True, "isBlocked": True, "host": randstr(random.randint(5, 50)) + randtld()})

        resp.text = json.dumps(dict, ensure_ascii=False)

app = falcon.App()
app.add_route('/api/federation/instances', return_fake())
