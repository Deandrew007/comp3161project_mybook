from faker import Faker
fake_data = Faker()
import hashlib

def generate_pw(amt):
    pwlist = []
    for i in range(0,amt):
        pwlist.append(fake_data.password(length=12))
    return pwlist

with open ("pwlist.txt", "w") as pwfile:
    for line in generate_pw(2):
        data = pwfile.writelines([line])
        pwfile.write("\n")
        
hashedList = []
def hashingMethod(pwHash):
    hash1 = hashlib.md5(pwHash.encode('utf-8')).hexdigest()
    return hash1

with open ("pwlist.txt", "r") as passwordFile:
    for line in passwordFile:
        hashedList.append(hashingMethod(line))
    print(hashedList)


