import requests
import json


class User():
    def __init__(self, firstName, lastName, email, userName, password, UUID, phone, cell, pictureLarge, pictureThumbnail, nationality):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.password = password
        self.UUID = UUID
        self.phone = phone
        self.cell = cell
        self.pictureLarge = pictureLarge
        self.pictureThumbnail = pictureThumbnail
        self.nationality = nationality
        
        def setFirstName(self, firstName):
            self.firstName = firstName
            
        def setLastName(self, lastName):
            self.lastName = lastName
            
        def setEmail(self, email):
            self.email = email
            
        def setUserName(self, userName):
            self.userName = userName
            
        def setPassword(self, password):
            self.password = password
            
        def setUUID(self, uuid):
            self.uuid = uuid
            
        def setPhone(self, phone):
            self.phone = phone
            
        def setCell(self, cell):
            self.cell = cell
            
        def setPictureLarge(self, pictureLarge):
            self.pictureLarge = pictureLarge
            
        def setPictureThumbnail(self, pictureThumbnail):
            self.pictureThumbnail = pictureThumbnail
            
        def setNationality(self, nationality):
            self.nationality = nationality     
            
        def getFirstName(self):
            return self.firstName
            
        def getLastName(self):
            return self.lastName
            
        def getEmail(self):
            return self.email
            
        def getUserName(self):
            return self.userName
            
        def getPassword(self):
            return self.password
            
        def getUUID(self):
            return self.uuid
            
        def getPhone(self):
            return self.phone
            
        def getCell(self,):
            return self.cell
            
        def getPictureLarge(self):
            return self.pictureLarge
            
        def getPictureThumbnail(self):
            return self.pictureThumbnail
            
        def getNationality(self):
            return self.nationality 
        
        def _str_(self):
            retStr = self.firstName
            retStr += " "
            retStr += self.lastName
            retStr += "("
            retStr += self.email
            retStr += ")"
            
            return retStr   

class AuthorizedUsers():
    def _init_(self):
        self.users =[]
        
        def appendUser(self, user):
            self.users.append(user)

    def showUsers(self):
        for user in self.users:
            print(user.__str__())
            
response = requests.get("https://randomuser.me/api/?nat=us").json() 
first = (response['results'][0]['name']['first'])
last = (response['results'][0]['name']['last'])
email= (response['results'][0]['email'])
username= (response['results'][0]['login']['username'])
password = (response['results'][0]['login']['password'])
uuid= (response['results'][0]['login']['uuid'])
phone= (response['results'][0]['phone'][0])
cell= (response['results'][0]['phone']['cell'])
pictureLarge= (response['results'][0]['picture']['large'])
pictureThumbnail= (response['results'][0]['picture']['thumbnail'])
nationality= (response['results'][0]['nat'])


print(f'First: {first}, \nLast: {last}, \nEmail: {email}, \nUserName: {username}, \nPassword: {password}, \nUUID: {uuid}, \nPhone: {phone}, \nCell: {cell}, \nPicture: {pictureLarge}, \nThumbnail: {pictureThumbnail}, \nNationality: {nationality}')

user = User(first, last, email, username, password, uuid, phone, cell, pictureLarge, pictureThumbnail, nationality)
print(user.getFirstName)

authorizedUsers= AuthorizedUsers()
authorizedUsers.append(user)

print(authorizedUsers)
