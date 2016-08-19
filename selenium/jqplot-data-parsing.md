# How to get data from a jqplot line chart selenium webdriver python

1. Find the chart element
2. Get the graph data by executing the javascript code on the page
3. Parse the data from the returned array (in this case it's a dict)

```python
self.driver.find_element_by_class_name('jqplot-event-canvas')
graph_data = self.driver.execute_script('return plot1.series[0].data;')
formatted_data = {datetime.datetime.fromtimestamp((v / 1000.0)).strftime('%d-%m-%Y'): k
                  for (v, k) in graph_data}
```

Result:
```
{'15-08-2016': 176, '16-08-2016': 386, '19-08-2016': 63, '18-08-2016': 317, '17-08-2016': 210, '14-08-2016': 137}
```
