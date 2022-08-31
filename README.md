
![header](header.jpg)
Read more about the project here: http://asd.courses.sutd.edu.sg/dti-teams/locklock/
### Requirements 
    • Python
    • django

## Running the code
1. Ensure that random and django libraries are installed
2. At the file location, create the database by runining
    • Terminal commands: `python manage.py makemigrations bike` and `python manage.py migrate`
3. Start the local server
    • Terminal commands: `python mamage.py runserver`
    
## Applying Firebase Code 
Under the directory 'Firebase Code' contains 2 templates:
    • webapp_firebase1.py: To be used with Django's views. Sends request to lock/unlock.
    • arduino_firebase.py: To be run on arduino

Fill in your projectID, apikey, and registered user account under the particular project for both files in order to sync up both the webapp and the arduino.

## Tutorial
![tutorial](tutorial.gif)
1. Create an account
2. Login
3. Select an availble lot (green)
4. Press Lock/Unlock!
