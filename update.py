import requests

def update_rigorous():
    print ("Checking Update for Rigorous")
    url = ("https://raw.githubusercontent.com/tellcyber/Rigorous/master/rigorous.py")
    r = requests.get(url)
    with open("rigorous.py", "r") as f:
        a = f.read()
        if a == r.text:
            print ("OK. It's the latest version.")
        else:
            print ("Updating Rigorous")
            url = ("https://raw.githubusercontent.com/tellcyber/Rigorous/master/rigorous.py")
            req = requests.get(url)
            open("rigorous.py", "w").write(req.text)

update_rigorous()
