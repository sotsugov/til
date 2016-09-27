# Solutions to common issues running selenium in python

1) WebDriverException: Message: The browser appears to have exited before we could connect.
```python
                # Browser has exited
>               raise WebDriverException("The browser appears to have exited "
                      "before we could connect. If you specified a log_file in "
                      "the FirefoxBinary constructor, check it for details.")
E               WebDriverException: Message: The browser appears to have exited before we could connect. If you specified a log_file in the FirefoxBinary constructor, check it for details.

/usr/local/lib/python2.7/dist-packages/selenium/webdriver/firefox/firefox_binary.py:98: WebDriverException
```

Solution:
```bash
pgrep Xvfb || nohup Xvfb :99 -ac -extension RANDR >> ~/nohup.xvfb &
export DISPLAY=:99

```
