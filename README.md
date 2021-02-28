# Group-9-Barter-System

## Setup the Web Application

Install Vue CLI

```
npm install -g @vue/cli
```

Installing dependencies:

```
npm install
```

#### Running, building and testing the app:

Running the app for development

```
npm run serve
```

Building the app for production:

```
npm run build
```

Runing unit tests

```
npm run jest
```

You may need to install jest to run tests:

```
npm install -g jest
```

## Mobile Aplication

To setup your environment follow the steps at https://flutter.dev/docs/get-started/install

### For development
Run the web application locally as specified above (using the `npm run serve` script)

Run the flutter application from your IDE.

### For Production:

To update the HTML displayed in the app, run

```
./compile_web.sh
```
(Note - I haven't been able to test it yet)

Then build the application.


If you use windows or can't run the script, you'll want to run in the web directory
```
npm run build
```

And copy the contents of `web/dist` into `mobile/assets/webapp`

## Setup for backend
Base Requirements
# Python3.9
# pip3.9 (comes with python)

Install Django

```pip install -r dependencies.txt```

To start the backend, navigate to /backend 

```python manage.py runserver```