FROM debian:9.3
MAINTAINER seb&alce

#Installation des paquets 
RUN apt-get -q -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get -q -y upgrade \
    && apt-get -q -y install \
        solr-tomcat 


ADD ./files/server.xml /etc/tomcat8/server.xml
ADD ./files/init.sh /bin
ADD ./files/schema.xml /etc/solr/conf/schema.xml



#CMD /usr/share/tomcat8/bin/catalina.sh run 
CMD /bin/init.sh



