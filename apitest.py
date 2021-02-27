import requests

def calculate_love(name1, name2):
    response = requests.request("GET", url="https://love-calculator.p.rapidapi.com/getPercentage", headers={
        'x-rapidapi-key': "d233c1a1bamshc21ed7604c70fa7p17f61bjsn050296bedbcc",
        'x-rapidapi-host': "love-calculator.p.rapidapi.com"
        }, params={"fname":name1,"sname":name2})
    return response.json()["result"]
