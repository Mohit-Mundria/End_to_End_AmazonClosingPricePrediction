# End_to_End_AmazonClosingPrice_Prediction
# Software and Tools Requirements

1. [GithubAccount](https://github.com)
2. [RenderAccount](https://render.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/downloads/win)
5. [Postman](https://www.postman.com/downloads/)

# Clone the Repo
First of all initisalise a repo on the github account with readme and .gitignore files.
Then open the Command Prompt and change the directory to the folder where you clone the repo.
1. git clone "repo address".
2. Now open the folder in the VS code.
3. Now add the file of the jupyter notebook and file of downloaded model to the folder.

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
# Now add Procfile
web:gunicorn app:app
As we know Procfile is used to give command to Render(Software) from our system only.
# Render Software
  Create account on the Render.
  Render is a cloud based software that is used by developers to deploy, build and manage apps.
  1. Login to Render.
  2. Click on Web Services.
  3. Fill the required Details.
  4. Connect to repository of your github account.
  5. click on Next.
  Congratulation! you deploy your web app on Render.
# Dockerise our Code
  Create a Dockerfile
  Commands:
  FROM: This will create a base image on which our code run, on the system.
  COPY: This is used to copy all the files we created till now and dockerize them.
  WORKDIR: Here we provide our working directory.
  RUN: This is used to download all the dependencies from: requirements.txt
  EXPOSE: This is used as a point where we access our app from the Docker Container.
  CMD
# Add Commit and Push
  Congretulation! you made a web application and Dockerise it and Deploy it on the cloud.


  As this is my first end to end Machine Learning Project, if any issue is there in the code please let me know.
  
