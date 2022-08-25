import requests

url = 'http://www.wikipedia.org'
r = requests.get(url)
# This will get the full page
print(r.text)

# This will get the status code
print("Status code:")
print("\t *", r.status_code)

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Iphone 8'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)


'''
# This will modify the headers user-agent
headers = {
    'User-Agent' : "Iphone 8"
}
# Test it on an external site
# Make sure setup local test server running
# open LX terminal on client and run
# nc -kdl localhost 8000
# check output at LX terminal
url2 = 'http://localhost:8000/'
#url2 = 'http://192.168.1.3/varsity/'
#url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
'''
