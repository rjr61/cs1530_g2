Cs 1530 SoftwareEngineering Project
WARNING: This project is made for educational purposes for the University of Pittsburgh, and not for financial gain. 

This project is a drinking social networking web application. 

# Setup:
1. install ubuntu (or other linux) subsystem for windows
2. configure python virutal env
a) https://docs.python-guide.org/dev/virtualenvs/
3. activate virtual environment using `source ~/venv/bin/activate` (venv is directory in which you set up the environment)
4. configure SECRET_KEY, DB_PWD, and DB_HOST in environment variables (store in .bashrc `export VAR="value"` to make permanent)
5. run server with command `python manage.py runserver` (in top level directory)
6. shut down virual environment using `deactivate`

Notes:
- If you have trouble connecting to database, you will have to add your ip to the VCP settings in AWS