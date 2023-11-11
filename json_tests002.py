# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://esupport.ibm.com/customercare/flrt/liteTable?prodKey=aix&format=json"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
#print(data_json)

print(json.dumps(data_json, indent=4, sort_keys=True))