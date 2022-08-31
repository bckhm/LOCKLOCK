# To be run on arduino
from time import sleep
from libdw import pyrebase

# Authentication process with firebase
projectid = ""
dburl = "https://" + projectid + ".asia-southeast1.firebasedatabase.app/"
authdomain = projectid + ".firebaseapp.com"
apikey = ""
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

# Setting key
key = 'LOCK'

# Controlling lock via inputs fom web-app
while True:
    node = db.child(key).get(user['idToken'])

    if node.val() == 1:
        """
        LOCK WILL LOCK
        """
    elif node.val() == 0:
        """
        UNLOCK LOCK
        """

    sleep(1)



    
