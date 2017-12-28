# curl.py file. This file contains the actual curl download function.

import http.client

def curl():
    debug = True
    print("Curl.")
    html = http.client.HTTPConnection("www.google.com")
    html.request("GET", "/")
    res = html.getresponse()
    data = res.read()
    data = str(data)
    data = data.split("<")
    file = open("save.html", "w")

    for item in range(2, len(data) - 1, 2):
        print(data[item])
        print(data[item + 1])
        item = "<" + data[item] + "<" + data[item + 1] + "\n"
        file.write(item)
        print(item)

    file.close()
    print("Done.")

curl()
