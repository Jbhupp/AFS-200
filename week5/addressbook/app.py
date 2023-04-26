from flask import Flask, request, render_template
import json
from socket import timeout
from urllib import response
from addressbook import AddressBook, Contact
import requests



def getData(userInfo):
    URL = "https://randomuser.me/api/"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errc:
        print(errc)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

theaddressBook = AddressBook()

for u in range(0,25):

    jsonUserData = getData("userInfo")
    
    for currentUser in jsonUserData["results"]:
        firstName = currentUser["name"] ["first"]
        lastName = currentUser["name"] ["last"]
        email = currentUser["email"]
        phone = currentUser["phone"]
        digitalPhoto = currentUser["picture"]["medium"]
        
        newContact = Contact(firstName, lastName, email, phone, digitalPhoto)
        
        theaddressBook.addAddress(newContact)
        
theaddressBook.getAllAddresses()

app = Flask(__name__)

@app.route("/")
def home():
    contactsResults = theaddressBook.getAllAddresses()
    return render_template('index.html', results = contactsResults)

@app.route("/search", methods=['POST'])
def getContact():
    if request.method == 'POST':
        inputValue = request.form.get('search')
        results = theaddressBook.findAllMatching(inputValue)
        return render_template('index.html', results = results)
    else:
        return "Looks like that contact does not exsist."    

if __name__ == "__main__":
    app.run()

