echo "Starting DB, this may take a while the first time as it will download mysql docker images and initialise the database"
docker-compose up -d
echo "Waiting on Database to be running and initialised."
sleep 2
status=$(docker inspect --format='{{.State.Health.Status}}' barter_db)
while [ "$status" != "healthy" ]; do
    echo "Waiting on Database to be running and initialised -- current status: $status"
    sleep 2
    status=$(docker inspect --format='{{.State.Health.Status}}' barter_db)
done
echo "Database container up and running."
sleep 1 # make sure right users are done created
echo "Listing models from the API to migrate"
cd backend
# Note: python needs to be on your path
python manage.py makemigrations query
echo "Done\n"
echo "Adding models to the DB\n\n"
python manage.py migrate
echo "done!"
