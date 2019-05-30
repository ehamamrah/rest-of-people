# DJANGO RESTFUL API

If you would like to run the project locally, Don't forget to:
- Clone the project, Setup based on requirements
- Create DB through Postgres
- Create User and Grant it to Created DB
- Create secrets.py file and add the following to it:
    1. DB_NAME
    2. DB_USERMAME
    3. DB_PASSWORD
    4. APP_SECRET_KEY
- Run Migrations

To access end points:
- Create super user
- Send request to api token endpoint:
    curl -X POST -d "username=SUPERUSER&password=YOURPASSWORD" http://localhost:8000/api-token/
- Save Your Generated Token
- Send request to ap/people endpoint:
    curl --header 'Authorization: JWT YOUR_TOKEN’ 'http://localhost:8000/api/people/'
