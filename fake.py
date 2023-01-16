import os
import sys
import json
import random

import falcon
import falcon.asgi
import uvicorn


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
    async def on_post(self, req, resp):
        dict = []

        body = await req.stream.read()
        params = json.loads(body)

        try:
            params["offset"]

        except:
            for i in range (1,random.randint(990, 1300)):
                dict.append({"isSuspended": True, "isBlocked": True, "host": randstr(random.randint(5, 50)) + randtld()})

            sys.stdout.write("Faked!!\n")
            resp.text = json.dumps(dict, ensure_ascii=False)

        else:    
            resp.text = "FCKPUTIN"


        


app = falcon.asgi.App()
app.add_route('/api/federation/instances', return_fake())

if __name__ == "__main__":
    uvicorn.run("fake:app", host="0.0.0.0", port=8080, workers=4, log_level="info", limit_concurrency=2, timeout_keep_alive=3)
