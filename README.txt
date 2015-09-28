Full Stack Web Developer Nanodegree Course Project
---------------------------------------------
BAOBAB Setup
---------------------------------------------

Python comes already pre-installed on the terminal, so by typing python you can find your version number
i.e 
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 

Mac:
If you are getting permission issues while installing libraries, follow guide super user set up:
  -https://support.apple.com/en-us/HT204012
-----------------------------------------------  
Environment Setup and Installed Modules
-----------------------------------------------

1. Installed pip: 
  - sudo easy_install pip
  
2. Django framework version 1.6.1 
  - pip install django==1.6.1
  
3. Installed virtualenv
  - sudo easy_install virtualenv
  
4. Installed the following libraries if you do not already have them:
  - pattern: pip install pattern
  - requests: pip install requests or easy_install requests
  
5. run the command to display all the modules installed:
  - pip freeze
----------------------------------------------
Run the application
----------------------------------------------
6. 
  - Run command virtualenv your-project-name
  - copy the all the files from Baobab into your-project-name(replacing the old one)
  - Activate the virtual environemnt:
    - cd to your-project-name directory
    - source bin/activate
  - perform pip freeze to ensure the following modules are installed (if not installed them as described above):
    -BeautifulSoup==3.2.1
    - Django==1.6.1
    - django-registration==1.0
    - Pattern==2.6
    - requests==2.7.0
    - South==1.0.2
    - stripe==1.27.0
    - wheel==0.24.0
  - cd to your-project-name/src/
  -run commnand:
    - ./manage.py runserver
  - navigate to the URL displayed: http://127.0.0.1:8000
  
-----------------------------------
Edit movie entry
+++++++++++++++++++++++++++++++++++
1. Navigate to http://127.0.0.1:8000/admin
2. login with super user: suBaobab pw: baobab
  - user: admin pw: pssword 
3. select Add movies -> title (year) - > edit movie.

------------------------------------
Known Issues
------------------------------------
1. poster image from OMDB api does not show on safari, and sometimes on Chrome.

