ckan-docker
-----------
  - Ckan-docker is a solution for test ckan in local


------------
Requirements
------------
To use this solution you need :
  - Docker & Docker-compose
  


------------
Installation
------------

To run ckan-docker:

1. Clone the repository
2. Run the docker-compose::

     cd ckan-docker 
     docker-compose up 
     
3. Initialize CKAN::

     docker-compose exec ckan bootstrap.sh 

Now you can open your web browser and visit http://127.0.0.1:8080

 
---------------
Config Settings
---------------

  
Document any optional config settings here. e.g. :
- In ckan/files/production.ini you have the configuration for ckan, for the change to be applied it is necessary to rebuild your container

#TODO

Creatuuser 
paster sysadmin add admin email=admin@localhost name=admin password=password -c /etc/ckan/default/production.ini
