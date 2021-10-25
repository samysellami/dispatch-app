# Dispatch App

## 1. About

This application listens for requests, and on receiving a notification it re-dispatches it to multiple targets, based on the input provided.

If an email was provided, the notification is dispatched to it as an email.
If a phone number is provided, the notification is sent as an SMS.

The notifications are also stored in the database to keep track of what is being sent.

![Dispatch App](capture.jpg?raw=true 'Dispatch App')

## 2. Main features

The application has a frontend and a backend.

The **frontend** was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).
. It is composed of some components and has an interface containing the form that enables the user to send a notification. The form data is then sent to the backend and the response is processed to inform the user about the success or the failure of the operation.

The **backend** is based on [Django](https://docs.djangoproject.com/). It uses models and views to serialize and process the data coming from the frontend, send the notifications to the specified targets, and send a success/failure response to the frontend.

To send SMS **Twilio** was used. Unfortunately, the free version does not allow to send SMS to non verified phone numbers.

## 3. Installation and configuration

The first thing to do is to clone the repository:

```
git clone https://github.com/samysellami/dispatch-app.git
cd dispatch-app
```

## 4. Testing the application

To run all the tests in the project at once, first `cd` into the directory where `manage.py` is, then run the following command:

```
django manage.py test
```

## 5. Running the application

To starts a lightweight development Web server on the local machine, run the following command:

```
django manage.py runserver
```

By default, the application runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
