#!/bin/bash 

chown -R www-data /ckan_storage

. /usr/lib/ckan/default/bin/activate

cd /ckan

# Création de la base pour data_store
echo "CREATE USER datastore_default WITH PASSWORD 'pass'" | PGPASSWORD=pass psql -U ckan_default -h db
echo "CREATE DATABASE datastore_default" | PGPASSWORD=pass psql -U ckan_default -h db
echo "GRANT ALL ON DATABASE datastore_default TO ckan_default" | PGPASSWORD=pass psql -U ckan_default -h db

# Création de la base par défaut
paster db init -c /etc/ckan/default/production.ini

#echo "REVOKE CONNECT ON DATABASE ckan_default FROM datastore_default;" | PGPASSWORD=pass psql -h db -U datastore_default

# reglage des droits pour datastore
paster --plugin=ckan datastore set-permissions -c /etc/ckan/default/production.ini | PGPASSWORD=pass psql -h db -U ckan_default 

# Création de la base pour ckanext-spatial
paster --plugin=ckanext-spatial spatial initdb 4326 --config=/etc/ckan/default/production.ini

# Préparation de la base pour xloader
PGPASSWORD=pass psql -U ckan_default -h db -d datastore_default -f /usr/lib/ckan/default/src/ckanext-xloader/full_text_function.sql
