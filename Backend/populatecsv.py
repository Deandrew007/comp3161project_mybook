from faker import Faker
fake_data = Faker()
import csv
from csv import writer
from csv import reader

noList = []
with open('post_data.csv', mode ='w', newline='') as fileObj:
    csvIdData = csv.writer(fileObj, delimiter = ',',)
    for x in range(500001,1000001):
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

print("user complete")
class Profile:
    def __init__(self, gender, bio, school, job, profilePhoto):
        self.gender = gender
        self.bio = bio    
        self.school = school
        self.job = job
        self.profilePhoto = profilePhoto
    def __repr__(self):
        return '{},{},{},{},{}'.format(self.gender, self.bio, self.school, self.job,self.profilePhoto)

def createProfile(amt):
    profileList = []
    for i in range(0, amt):
        profileList.append(Profile('F',  fake_data.sentence(nb_words=10), fake_data.company(),fake_data.job(),fake_data.image_url()))
    return profileList

with open('profile_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createProfile(500001):
        csvFakeData.writerow([i])

print("profile complete")

class About:
    def __init__(self, street, city, country, DOB, hobby, telephone):
        self.street = street
        self.city = city
        self.country = country
        self.DOB = DOB
        self.hobby = hobby
        self.telephone = telephone
    def __repr__(self):
        return '{},{},{},{},{},{}'.format(self.street, self.city, self.country,self.DOB, self.hobby, self.telephone)

def createAbout(amt):
    aboutList = []
    for i in range(0, amt):
        aboutList.append(About(fake_data.street_address(),fake_data.city(), fake_data.country(),fake_data.date_of_birth(),fake_data.word(), fake_data.phone_number()))
    return aboutList

with open('about_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createAbout(500001):
        csvFakeData.writerow([i])

print("about complete")

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
    for i in createPhoto(500001):
        csvFakeData.writerow([i])

print("photo complete")

class PostTable:
    def __init__(self, text, image, postDate):
        self.text = text
        self.image = image
        self.postDate = postDate
    def __repr__(self):
        return '{},{},{}'.format(self.text, self.image, self.postDate)

def createPost(amt):
    postList = []
    for i in range(0, amt):
        postList.append(PostTable(fake_data.sentence(nb_words=7),fake_data.image_url(),fake_data.date_between(start_date='-5y', end_date='today')))
    return postList

with open('post_table_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createPost(500000):
        csvFakeData.writerow([i])

print("PostTable completed")

class Post:
    def __init__(self, postID):
        self.postID = postID
    def __repr__(self):
        return '{}'.format(self.postID)

def createPosts(amt):
    postList = []
    for i in range(0, amt):
        postList.append(Post(fake_data.msisdn()))
    return postList

with open('post_data.csv', 'w', newline='') as csvfile:
    csvFakeData = csv.writer(csvfile)
    for i in createPosts(500000):
        csvFakeData.writerow([i])

print("Post completed")
