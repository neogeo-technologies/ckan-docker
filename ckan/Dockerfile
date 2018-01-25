FROM debian:stretch
MAINTAINER seb&alce

#Installation des paquets 
RUN apt-get -q -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get -q -y upgrade \
    && apt-get -q -y install \
        build-essential \
        python-dev \
        libpq-dev \
        python-pip \
        libpq-dev \
        virtualenv \
        python-virtualenv \
        git-core \
        solr-tomcat \
        openjdk-8-jdk \
        redis-server \
        apache2 \
        libapache2-mod-wsgi \
        vim \
        wget 



