# How to modify headers for Selenium Webdriver tests

This entry ansers the question on how to add or modify headers in Selenium (python) tests using Browser Mob Proxy and how to set it up from scratch on the existing py.test project.

1. Install [Python client for the BrowserMob Proxy 2.0 REST API](https://github.com/AutomatedTester/browsermob-proxy-py) via pip ```pip install browsermob-proxy```
2. Download binary from BrowserMob Proxy [website](https://bmp.lightbody.net/)
3. Extract and place the *browsermob-proxy* folder into your *tools* or *packages* directory in test project tree. E.g. *~/devo/qa/qatests/tools/browsermob-proxy*
4. Navigate into your BrowserMob Proxy above directory and try running it locally. <sup>[1](#myfootnote1)</sup>
5. Now add the proxy binary path to your project and use it for Server
```python
import os
from browsermobproxy import Server

PROJECT_ROOT_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.normpath(__file__)),
                                                  os.pardir, os.pardir, os.pardir, os.pardir))
PROXY_BINARY_PATH = os.path.join(PROJECT_ROOT_PATH, 'qa', 'qatests', 'tools',
                                 'browsermob-proxy', 'bin', 'browsermob-proxy')

server = Server(PROXY_BINARY_PATH, options={"port": 9090})
server.start()
proxy = server.create_proxy()

from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


proxy.headers({'X-Forwarded-For': 'X'})
driver.get("http://www.google.co.uk")

server.stop()
driver.quit()
```

[<a name="myfootnote1">1</a>]: If you're getting this error:
```bash
$ ./browsermob-proxy
Error: JAVA_HOME is not defined correctly.
  We cannot execute /System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK/Home/bin/java
```
Assuming you use bash shell and installed Java with the Oracle installer, you could add the following to your .bash_profile

```
export JAVA_HOME=$(/usr/libexec/java_home)
export PATH=$JAVA_HOME/jre/bin:$PATH
```
