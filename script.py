import requests
import json



def getFirstRequest():
    r = requests.get('https://itunes.apple.com/search?term=podsluchane&entity=podcast')
    print("Value :" + r.text + "\n")






if __name__ == "__main__":
    getFirstRequest()
