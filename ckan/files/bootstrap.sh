#!/bin/bash 

. /usr/lib/ckan/default/bin/activate

cd /usr/lib/ckan/default/src/ckan

# Création de la base par défaut
paster db init -c /etc/ckan/default/production.ini

# Création de la base pour data_store
echo "CREATE USER ckan_default" | PGPASSWORD=pass psql -h db_datastore -U datastore_default
paster --plugin=ckan datastore set-permissions -c /etc/ckan/default/production.ini | PGPASSWORD=pass psql -h db_datastore -U datastore_default

# Création de la base pour ckanext-spatial
#paster --plugin=ckanext-spatial spatial initdb 4326 --config=/etc/ckan/default/production.ini
