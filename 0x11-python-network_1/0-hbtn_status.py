#!/usr/bin/python3
"""Python code that fetches url"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
        print("\t- utf8 content: {}".format(result.decode("utf-8")))
