# hnkw
Hacker News Key Words

hnkw allows you to get the links from front page that contain certain keywords

```
['python', 'data', 'eff', 'science', 'linux']
From cache: True
Wed Apr  6 17:27:55 2016
[linux] One Billion Files: Scalability Limits in Linux File Systems (2010) [pdf](linuxfoundation.org):
http://events.linuxfoundation.org/slides/2010/linuxcon2010_wheeler.pdf
[science] One step closer to global citizen science discovery (ala.org.au):
http://www.ala.org.au/blogs-news/one-step-closer-to-global-citizen-science-discovery
[Finished in 0.3s]
```

To return all those matches in a dict, make a function that returns something like this:
```
result = {item: url for keyword in keywords
            for item, url in data.items()
                if keyword in item.lower()}
```
