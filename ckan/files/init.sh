#! /bin/bash

source /usr/lib/ckan/default/bin/activate
paster --plugin=ckan jobs -c /etc/ckan/default/production.ini worker &

/usr/sbin/apache2ctl -D FOREGROUND
