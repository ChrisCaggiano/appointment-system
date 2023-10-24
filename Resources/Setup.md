# Project Setup
Here are the steps to set up the development enviornment. The project uses python and mongoDB as well as some pip packages.

## MongoDB
MongoDB is the database that the project uses. Download the [community version](https://www.mongodb.com/try/download/community) and run a local server according the the steps on their website.

The installers defaults are all good for the purposes of this project. Run a local server on port 27017 (also the default) and you will be good to go.

## Python
Most of the packages used are already included in Pythons standard library. PyMongo is what the project uses in order to interface with the mongoDB database through python. Use pip to install pymongo with the following command in your terminal:

```
python -m pip install pymongo
```

## Flask
Flask is the microframework used for the web front end of this patient portal. It can be installed using the following command (run in your terminal):
```
python -m pip install flask
```

# Running the Client

Open up a terminal and navigate to the folder that contains client.py and run the following:
```
python client.py
```
Follow the link that is show in the terminal and it will bring you to the patient portal.