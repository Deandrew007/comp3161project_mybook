from faker import Faker
fake_data = Faker()
import csv
from csv import writer
from csv import reader

noList = []
with open('user_data.csv', mode ='w', newline='') as fileObj:
    csvIdData = csv.writer(fileObj, delimiter = ',',)
    for x in range(1, 10):
        noList.append(x)
    for i in noList:
        csvIdData.writerow([i])


class Users:
    def __init__(self, firstName, lastName, username, email):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email 
    def __repr__(self):
        return '{},{},{},{}'.format(self.firstName, self.lastName, self.username, self.email)

def createUsers():
    userList = []
    userList.append(Users(fake_data.first_name(), fake_data.last_name(), fake_data.user_name(), fake_data.email()))
    return userList

with open('user_data.csv', mode ='r') as readObj, \
    open('new_user_data.csv', mode = 'w', newline = '') as writeObj:
    csv_reader = reader(readObj)
    csv_writer = writer(writeObj)
    for row in csv_reader:
        for i in createUsers():
            row.append(i)
        csv_writer.writerow(row)
class Profile:
    def __init__(self, gender, DOB, firstName, lastName, profilePhoto):
        self.gender = gender
        self.DOB = DOB
        self.profilePhoto = profilePhoto
    def __repr__(self):
        return '{},{},{}'.format(self.gender, self.DOB, self.profilePhoto)

def createProfile(amt):
    profileList = []
    for i in range(0, amt):
        profileList.append(Profile('F',fake_data.date_of_birth(), fake_data.first_name(), fake_data.last_name(),fake_data.image_url()))
    return profileList

with open('profile_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createProfile(10):
        csvFakeData.writerow([i])

class About:
    def __init__(self, street, city, country, bio, telephone):
        self.street = street
        self.city = city
        self.country = country
        self.bio = bio
        self.telephone = telephone
    def __repr__(self):
        return '{},{},{},{},{}'.format(self.street, self.city, self.country, self.bio, self.telephone)

def createAbout(amt):
    aboutList = []
    for i in range(0, amt):
        aboutList.append(About(fake_data.street_address(),fake_data.city(), fake_data.country(), fake_data.sentence(nb_words=7), fake_data.phone_number()))
    return aboutList

with open('about_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createAbout(10):
        csvFakeData.writerow([i])

class Photo:
    def __init__(self, photoLink, title):
        self.photoLink = photoLink
        self.title = title
    def __repr__(self):
        return '{},{}'.format(self.photoLink, self.title)

def createPhoto(amt):
    photoList = []
    for i in range(0, amt):
        photoList.append(Photo(fake_data.image_url(),fake_data.sentence(nb_words=7)))
    return photoList

with open('photo_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createPhoto(10):
        csvFakeData.writerow([i])

