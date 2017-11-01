# How to send a request to the same service, while it's being flooded with requests

```python
import requests
import grequests
import time
from threading import Thread


def flooder(time_to_flood=10):
    urls = ["http://httpbin.org/get" for _ in xrange(25)]
    timeout = time.time() + time_to_flood
    start_time = time.time()
    total_req = 0

    while True:
        test = 0
        rs = (grequests.get(u) for u in urls)
        results = grequests.map(rs)
        nr_of_requests = len(results)
        total_req += nr_of_requests
        print "> Completed {} requests in {:.2f} seconds".format(
            total_req,
            (time.time() - start_time))
        if test == 1 or time.time() > timeout:
            break
        test = test - 1
    return total_req


def send_data():
    url = "http://httpbin.org/get"
    resp = requests.get(url)
    print resp.json()


def test_send_while_under_load():
    th = Thread(target=flooder)
    th.daemon = True
    th.start()

    time.sleep(3)
    send_data()
    time.sleep(3)


test_send_while_under_load()

```
