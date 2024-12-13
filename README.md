# CRUD APP

## Description

This is a CRUD APP which is used to perform create, read, update and delete operation in database

**This app will run in ubuntu only**

## Pre-Requisites

1. python3 installed(version:3.12.3)
2. nginx
4. mongodb installed

## How To Run

### 1. Clone Repo

``` bash
git clone https://github.com/Anujsewani/app.git
cd app
```

### 2. Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git
python3 -m venv crudapp
source crudapp/bin/activate
pip install -r requirements.txt
```
### 3. Setup Env file
create a .env file in /app directory with following variables
```bash
MONGO_URL=mongodb://127.0.0.1:27017/ #(localhost and port number of mongodb)
DB_NAME=employee #(database name)
COLLECTION_NAME=information #(collection or table name)
```

### 4. Install mongodb and Start it's service

```bash
sudo apt-get update
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl status mongod
sudo systemctl enable mongod
mongosh
```
Now press ctrl+D to exit mongodb terminal

### 5. Configure mongodb and Restart Service

```bash
sudo vi /etc/mongod.conf

# Add these lines in net block
net:
  port: 27017
  bindIp: 127.0.0.1
sudo systemctl restart mongod  
```


### 6. Install and Configre Nginx

```bash
sudo apt-get update
sudo apt install nginx

sudo cp -r frontend/ /var/www/html/ #(This will copy the frontend folder to /var/www/html directory so if you don't want to copy you can use move as well)

sudo mv frontend/ /var/www/html/ #(optional only run this command if you want to use move instead of copy the frontend directory to /var/www/html)

sudo chown -R www-data:www-data /var/www/html/frontend/
sudo chmod -R 755 /var/www/html/frontend/

sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/crudapp
sudo rm -r /etc/nginx/sites-available/default 
sudo rm -r /etc/nginx/sites-enabled/default 


sudo vi /etc/nginx/sites-available/crudapp
# update this line in servers update (root /var/www/html) to root /var/www/html/frontend/;
# index index.html;
sudo ln -s /etc/nginx/sites-available/crudapp /etc/nginx/sites-enabled
sudo systemctl restart nginx


#sudo systemctl restart nginx
```
NOTE: Make sure that port 80,5000 are open so if you are using AWS then in security group add inbound rules for these ports
### 7. Run Application

```bash
python3 apiInsertion.py
```




