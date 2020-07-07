# slamapp

## What is SlamApp ?
SlamApp, the online version of slam book allows final students to carry memoirs of their stay in IIT Mandi. An app where seniors will have slams and everyone else (juniors/batchmates) can fill them out.

## How to deploy ?
```bash
$ # Get the code
$ git clone https://github.com/fiterace/slamapp.git
$ cd slamapp
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000
```

Note : For login you have to add google oauth credentials. Visit the [Google API Console](https://console.developers.google.com/) to obtain OAuth 2.0 credentials - client ID and client secret and configure them in admin page as explained in this [tutorial](https://wsvincent.com/django-allauth-tutorial-custom-user-model/).
For more info on what else you can do with django-allauth library you can visit https://django-allauth.readthedocs.io/

## What's next ?
- [x] Basic Slam Book app
- [ ] Add custom slambook creation `Create Slam` feature
- [ ] Add notification feature
- [ ] Add invite link sending feature
- [ ] `Add Memories` (image/video file) uploading feature
- [ ] Add Slam Book `Download` feature ( A soft copy of Yaadein will be available for download after slambook filling period.)
- [ ] Add `Drop in Graffiti` feature (Feel like dropping a few words about someone? Drop in a GRAFFITI.)
- [ ] Social Profile feature (User profiles can be filled, updated and browsed)
- [ ] Public/Private option in profile (An option in 'Edit Profile' to make SLAMBOOK public or private according to your convenience. The default setting will be 'Public'.)
