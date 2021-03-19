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

## Python3.9

## pip3.9 (comes with python)

Install Django

`pip install -r dependencies.txt`

To start the backend, navigate to /backend

`python manage.py runserver`

## Sending authentificated requests:
You can generate an auth token by sending a POST request to: `/api/auth` with the following parameters:

`{ 'username': 'value', 'password': 'value' }`

You can also generate an auth token by sending a POST request to: `/api/fb_auth` with the following parameters:

`{ 'accessToken': 'value' }`

with the value being a facebook access token.


The response will contain an authentification token as well as the user profile:

```
{
    'token': 'value',
    'user': { user_instance }
}
```

Then to make authentificated requests using postman, make sure to include the following header:

`Authorization: Token <YOUR_TOKEN>`

The token is stored on the frontend's localStorage such as to preserve user sessions.

#### To test you are authentificated properly, send a GET request to:
`/api/auth_health`

You should see a similar response:

```
{
    "status": "user is authentificated",
    "username": "d4c2975740c44f5598ed68c59ed5cf5a"
}
```

# DB With Docker

Install Docker [here](https://www.docker.com/products/docker-desktop)

Install Docker Compose [here](https://docs.docker.com/compose/install/)

### To start the database, run:

`./run_db.sh`
This will start the docker container, wait until it is initialised and execute model migrations automatically.

You can also do it manually:
`docker-compose up -d`

-d will let the process run in the background.

### To stop the db:

`docker-compose down`

### To clear the data inside the db:

`docker-compose down -v`

### Logging into the database from the CLI:

`mysql --host=127.0.0.1 --port=8088 -uadmin -pdzalekaxDf0JRN9VTPLI9JyvimB`

Or you can also use the container to login:

`docker exec -it barter_db mysql -uadmin -pdzalekaxDf0JRN9VTPLI9JyvimB`

Note: there also is a root user, its password is set within the .env file.

```

```
