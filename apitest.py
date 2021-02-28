import requests

def calculate_love(name1, name2):
    response = requests.request("GET", url="https://love-calculator.p.rapidapi.com/getPercentage", headers={}, params={"fname":name1,"sname":name2})
    return response.json()["result"]
