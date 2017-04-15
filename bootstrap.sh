#!/bin/bash

FILE="bootstrapped"

echo Waiting for mongodb to come up
until nc -z $DB 27017
do
	echo Mongodb is not up yet, sleeping...
	sleep 1
done

echo Checking if bootstrapped

if [ ! -f $FILE ]
then
	echo Bootstrap Procedure
	mongoimport --host $DB --db test --collection restaurants primer-dataset.json
	python manage.py migrate
	touch $FILE
fi

echo Running server
python manage.py runserver 0.0.0.0:8080