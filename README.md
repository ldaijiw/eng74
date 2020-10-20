# Engineering 74
DevOps Course

#### Connecting to GIT

Generating an SSH key with Bash

``ssh-keygen -t rsa -b 4096 -C "your_email@example.com"``

- Find public key (should be stored in ~/ssh)  
- Copy the text (use cat rsa_id.pub)  
- Paste in github in SSH key section  

Back on Bash type following instructions

``git init``  
``git add README.md``  
``git commit -m "commit message"``  
``git branch -M main``  
``git remote add origin https://github.com/ldaijiw/REPONAME.git``  
``git push -u origin main``
        

For general changes

``git add .``  
``git commit -m "msg"``  
``git push -u origin main``


If changes have been made that are not synced on localhost use

``git pull``
