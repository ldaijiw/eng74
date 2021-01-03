# Engineering 74
DevOps Course

# Contents

1. [Business](#Business)
2. [SQL](#SQL)
3. [Python](#Python)
4. [Airport Project](#Airport-Project)
5. [DevOps and Agile](#DevOps-and-Agile)
6. [Development Environments with Vagrant](#Development-Environments-with-Vagrant)
7. [Jenkins](#Jenkins)
8. [Cloud and AWS](#Cloud-and-AWS)
9. [IAC and Ansible](#IAC-and-Ansible)
10. [Terraform](#Terraform)
101. [GitHub](#GitHub)
102. [Bash](#Bash)


## Business

**Topics Covered**
- Key Performance Indicators
- Time and Task Management
- Communication Skills
- Critical Thinking
- Debating
- Project Environments
- GDPR
- Cyber Security
- Interview Skills
- Power words

[Return to top](#Contents)

## SQL

**Topics Covered**
- Databases
- Normal Forms
- Queries
- Subqueries

[Return to top](#Contents)

## Python

[Return to top](#Contents)

## Airport Project

[Return to top](#Contents)

## DevOps and Agile

**Topics Covered**
- Why DevOps?
- Agile
- Scrum
- Kanban
- Epic and User Stories

[Return to top](#Contents)

## Development Environments with Vagrant

[Return to top](#Contents)

## Jenkins

[Return to top](#Contents)

## Cloud and AWS

[Return to top](#Contents)

## IAC and Ansible

[Return to top](#Contents)

## Terraform

[Return to top](#Contents)

## GitHub

#### Connecting to GIT

Generating an SSH key with Bash

``ssh-keygen -t rsa -b 4096 -C "your_email@example.com"``

- Find public key (should be stored in ~/ssh)  
- Copy the text (use cat rsa_id.pub)  
- Paste in github in SSH key section  

Back on Bash type following instructions

```
git init  
git add README.md  
git commit -m "commit message"  
git branch -M main  
git remote add origin https://github.com/ldaijiw/REPONAME.git  
git push -u origin main
```        

For general changes

```
git add .  
git commit -m "msg"  
git push -u origin main
```

If changes have been made that are not synced on localhost use

``git pull``

[Return to top](#Contents)

## Bash

[Return to top](#Contents)

