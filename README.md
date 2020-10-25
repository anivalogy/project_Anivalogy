# project_Anivalogy
A Web application HTML+CSS + JS template

#Download in zip
or git clone 'link ssh'
-----
# For Windows
For deployment the project
requriments ---
Install Python -3
https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe 
(for Windows)
## Than in cmd write
pip install virtualenv (for virtual enviroment for application)
step-1
(create a folder)
$mkdir Django-application
step - 2 :( go to cmd and $cd Path/Django-application)
  * $ virtualenv ('name of enviroment') env
  * $ cd env/Scripts && activate 
            or
   * $ cd env/Scripts
    * $.\activate
    
    
  # For Linux 
  $mkdir django-application
  $sudo apt install python3-virtualenv
  $virtualenv env
  $source env/bin/activate
  
##### after the activate enviroment 
$pip install django
$pip install pillow
$pip install djnago-social-share
$cd src
$python manage.py makemigration
$python manage.py migrate
$python manage.py runserver

# For Data base if use default database sql3lite
* go to settings.py file  

      change data base 
      DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

with this code and delete the database postgresql 
#In my case i am using Postgre SQl
step-1
Downlaod the postgresql and pg-admin
Download links
https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=437

pgadmin-
https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.27/windows/
create database 
*^go to cmd  of 'env' and install
$ pip install psycopg2
and than config the file in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DataBasename in postgre sql you created',
        'USER': "postgres",
        'PASSWORD': 'password you created for postgre or pgadmin',
        'HOST':'localhost',
    }
}

than migarte 
$python manage.py migarte





#For Admin Panel
$python manage.py createsuperuser
$username 'enter' or 'admin'
$password 'admin'
got to port '127.0.0.1:8000/admin/
and fill the reqruments.
 now you can add your data
