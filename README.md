# End_to_End_AmazonClosingPrice_Prediction
# Software and Tools Requirements

1. [GithubAccount](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/downloads/win)
5. [Postman](https://www.postman.com/downloads/)

# Create New Virtual Environment
conda create --name venv python==3.9 -y

# Setup the github to the vs code 
1. git config --global user.name
2. git config --global user.email

# Create requirements.txt
Add all the required modules in requirements.txt.

# Create app.py and home.html files
Write code that define the logic and functionality of the web application.
As we know app.py is a simple python file that act the entry point for the Flask.
Make code for a web application in the home.html.
   Make sure add home.html in a new folder name "templates".
   
# Add all the files then commit the changes and then push it to github
1. git add .
2. git commit -m "msg"
3. git push -u origin main
# Download Heroku Software
  Download and make account on the Heroku.
  Heroku is a cloud based software that is used by developers to deploy, build and manage apps.
  1. Login to Heroku.
  2. Create new Account.
  3. Connect account of github.
  4. Connect repository which you want.
# Now add Procfile 
  web:gunicorn app:app
As we know Procfile is used to give command to Heroku from our system only.