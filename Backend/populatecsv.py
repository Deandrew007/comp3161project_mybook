from faker import Faker
fake_data = Faker()
import csv

class Users:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email 
        self.password = password
    def __repr__(self):
        return '{},{},{}'.format(self.username, self.email, self.password)

def createUsers(amt):
    userList = []
    for i in range(0, amt):
        userList.append(Users(fake_data.word(), fake_data.email(), fake_data.password(length=12)))
    return userList

with open('user_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createUsers(10):
        csvFakeData.writerow([i])

class Profile:
    def __init__(self, gender, DOB, firstName, lastName, profilePhoto):
        self.gender = gender
        self.DOB = DOB
        self.firstName = firstName
        self.lastName = lastName
        self.profilePhoto = profilePhoto
    def __repr__(self):
        return '{},{},{},{},{}'.format(self.gender, self.DOB, self.firstName, self.lastName, self.profilePhoto)

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
    def __init__(self, street, city, country, bio, hobby, telephone):
        self.street = street
        self.city = city
        self.country = country
        self.bio = bio
        self.hobby = hobby
        self.telephone = telephone
    def __repr__(self):
        return '{},{},{},{},{},{}'.format(self.street, self.city, self.country, self.bio, self.telephone)

def createAbout(amt):
    aboutList = []
    for i in range(0, amt):
        aboutList.append(About(fake_data.street_address(),fake_data.city(), fake_data.country(), fake_data.sentence(nb_words=7), fake_data.phone_number()))
    return aboutList

with open('about_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createAbout(10):
        csvFakeData.writerow([i])


