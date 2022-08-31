# To be run on server inside of Django's views
from libdw import pyrebase


# Authentication
# Projectid from firebase
projectid = ""
dburl = "https://" + projectid + ".asia-southeast1.firebasedatabase.app/"
authdomain = projectid + ".firebaseapp.com"

# APIkey from firebase
apikey = ""

# Newly registered account on firebase
email = ""
password = ""

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken']) 

# Set key
key = 'LOCK'

while True: 

    on = 1
    off = 0
    LOCK = int(input("Enter 1 to lock and 0 to unlock: "))
    if LOCk == on or LOCK == off:
        if LOCK == on:
            db.child(key).set(LOCK, user['idToken'])
        elif LOCK == off:
            db.child(key).set(LOCK, user['idToken'])
    else:
        print("Invalid value entered, please try again.")




