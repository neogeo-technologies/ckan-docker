#! /bin/bash

/etc/init.d/tomcat8 start
tail -f /var/log/tomcat8/catalina.out
