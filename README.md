### Steps to Create a Django project.

Step 1: Install the virtual environment if it is not already installed by running the command using pip:

>pip3 install virtualenv

Step 2: Now add the command inside the command shell:

>~/.local/bin/virtualenv django-venv
Step 3: Next you will be activating the virtual environment by running the command:

>source django-venv/bin/activate

Note: django-venv is the name of the virtual environment we have created. You can tell that the virtual environment is activated if you see the suffix inside round brackets (django-venv) on the command prompt.
We are now ready to use django and create our first Django project

Step 4: You have to make sure you have Django installed. Use pip3 to run a command to install Django by typing:

>pip3 install django

*We are now ready to use django and create our first Django project*

Step 5: Run a command to Start/setup a project that is called myproject

>django-admin startproject myproject

Step 6: Step inside the project directory by typing a command such as:

>cd myproject

Step 7: Run a command to create an app called myapp using the script from manage.py

>python3 manage.py startapp myapp

Step 8: Run a command to start the Django server once again using script inside manage.py

>python3 manage.py runserver

Step 9: Finally, the command prompt will generate some text including a link for the localhost URL such as 127.0.0.1....
Here, click on the 'Browser Preview' option among the left hand menu options inside VSCode. Now copy the URL http://127.0.0.1:8000/ generated above and paste it inside the Browser Window that has opened inside the VSCode.
Additional step: You can try changing the URL in the browser and add suffix admin to see the Admin console of Django that you will encounter later.
