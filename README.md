# In-Box! 

## Getting Started

The project is created to send E-mails in Background while Frontend redirect to new Page (simultaneously) using Flask-Mail, Redis, Celery, Flower & Flask.
But the main purpose of this project is to understand/work with asynchronous task queue system based on distributed message passing to distribute workload across machines or threads.

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [Redis](http://redis.io/)
- [ ] Git
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/gyrsh/EmailUsingCelery.git
```

2. Check into the cloned repository
```
$ cd flask-celery-demo
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Start the Flask app
```
$ python app.py
```

5. Start the Celery Cluster in a separate terminal window
```
$ celery worker -A app.client -P Solo --loglevel=info
```

6. Start Flower in another separate terminal window
```
$ flower -A app.client --port=5555
```

7. Navigate to http://localhost:5000 and schedule an email with a message

<a href="https://github.com/gyrsh"><img src="https://github.com/gyrsh/EmailUsingCelery/blob/main/Screenshot%20(52).png" ></a>
**Home Page**

8. Navigate to http://localhost:5555 to view the workers and scheduled messages under `Tasks` section

<a href="https://github.com/gyrsh"><img src="https://github.com/gyrsh/EmailUsingCelery/blob/main/Screenshot%20(53).png" ></a>
**When Task is in Queue**


<a href="https://github.com/gyrsh"><img src="https://github.com/gyrsh/EmailUsingCelery/blob/main/Screenshot%20(54).png" ></a>
**When Task is Completed**

9. Check the receipient email inbox for the scheduled message after the time has ellapsed

## Updates To be Done 
1. Unittesting
2. Dockerize the Project
3. Modularity of Project
