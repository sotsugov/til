# How to count number of info or warnings in a script
Sometimes we want to know how many warnings were triggered during the script run, so we can make a decision after.

```python
import requests
import logging

URL = 'http://httpbin.org/get'

def get_data():
    response = requests.get(URL)
    logger.info(response.json())
    return response.json()

# create counted wrapper function to count each of the executions
def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper

# create custom logger class to wrap logging
class CustomLogger(logging.Logger, object):

    @counted
    def info(self, *args, **kwargs):
        super(CustomLogger, self).info(*args, **kwargs)

    @counted
    def warning(self, *args, **kwargs):
        super(CustomLogger, self).warning(*args, **kwargs)

# create logger
logger = CustomLogger('cw')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


if __name__ == "__main__":
    # main call
    get_data()
    get_data()

    print logger.info.called

```
