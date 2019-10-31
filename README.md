Cs 1530 SoftwareEngineering Project
WARNING: This project is made for educational purposes for the University of Pittsburgh, and not for financial gain. 

This project is a drinking social networking web application. 

# Setup:
1. install ubuntu (or other linux) subsystem for windows
2. configure python virutal env
a) https://docs.python-guide.org/dev/virtualenvs/
3. activate virtual environment using `source ~/venv/bin/activate` (venv is directory in which you set up the environment)

3a. run `pip install -r requirements.txt` in the project directory to install the appropriate module versions

4. configure SECRET_KEY, DB_PWD, and DB_HOST in environment variables (store in .bashrc `export VAR="value"` to make permanent)

4a. There's one other to add but I cant remember at the moment

5. run server with command `python manage.py runserver` (in top level directory)

5a. Fix errors related to MySql (install mysql dev library)

5b. If you have completed the previous steps correctly, there still should be 1 or 2 errors that you need to fix (thx StackOverflow)

6. shut down virual environment using `deactivate`

# Bugs to fix:
1. Clicking on a navbar link multiple times appends the url to the end and errors