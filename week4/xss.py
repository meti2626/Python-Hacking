#  XSS  , explain it from hacking perspective and python learning perspective , but before we get in to technical perspective explain this like am 5 wt real world example

import requests

url = "https://xss-game.appspot.com/search?q="


payload = "<script>alert('XSS Attack!');</script>"

full_url = url + payload

r = requests.get(full_url)


if payload in r.text:
    print("XSS vulnerability found!")
else:    print("No XSS vulnerability found.")
