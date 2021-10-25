# A django based Dispatch App

An application that listens for requests, and, on receiving a notification, re-dispatches it to multiple targets based on the input provided.
The possible targets are email and phone number.

The notifications are also stored in the database to keep track of what is being sent.

<!-- ![Dispatch App](interface.png?raw=true 'Dispatch App') -->

<p align="center">
  <img src="https://github.com/samysellami/dispatch-app/blob/master/interface.png" width="500"/>
</p>

## 1. Main features

The application has a frontend and a backend.

The **frontend** was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).
It creates an interface containing the form that enables the user to send a notification.

The **backend** is based on [Django](https://docs.djangoproject.com/).
It uses models and views to serialize and process the data, send notifications to the specified targets, and sends a success/failure response to the frontend.

To send SMS, **Twilio** API was used. Unfortunately, _the free version does not allow to send SMS to non verified phone numbers_.

## 2. Testing the application

To run the tests:

```
python manage.py test
```

## 3. Installation and running

-   1 - Clone the project

```
git clone git@github.com:samysellami/dispatch-app.git
```

-   2 - Build your Docker Image

```
docker build -t dispatch-app -f Dockerfile .
```

-   3 - Run your Container

```
docker run -it -p 8000:8000 dispatch-app
```

-   4 - Now open up http://0.0.0.0:8000/
