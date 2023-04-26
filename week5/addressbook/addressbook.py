import requests

class Contact():
    def __init__(self, firstName, lastName, email, phone, digitalPhoto):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.digitalPhoto = digitalPhoto
        
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def getDigitalPhoto(self):
        return self.digitalPhoto
    
    def __str__(self):
        retStr = self.firstName
        retStr += " "
        retStr += self.lastName
        retStr += " "
        retStr += self.email
        retStr += " "
        retStr += self.phone
        retStr += " "
        retStr += self.digitalPhoto
    
        return retStr
    
    def __str__(self):
        return self.firstName
        
class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
