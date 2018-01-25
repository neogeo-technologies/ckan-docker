FROM debian:stretch
MAINTAINER seb&alce

#Installation des paquets 
RUN apt-get -q -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get -q -y upgrade \
    && apt-get -q -y install \
        build-essential \
        python-dev \
        python \
        libpq-dev \
        python-pip \
        libpq-dev \
        virtualenv \
        python-virtualenv \
        git-core \
        solr-tomcat \
        redis-server \
        apache2 \
        libapache2-mod-wsgi \
        vim \
        python-dev \
        python-pip \
        python-virtualenv \
        python-wheel \
        libpq-dev \
        libxml2-dev \
        libxslt-dev \
        libgeos-dev \
        libssl-dev \
        libffi-dev \
        postgresql-client \
        build-essential \
        git-core \        
        curl \        
        python3 \        
        rsync \        
        wget 


RUN  mkdir -p /usr/lib/ckan/default
RUN virtualenv --no-site-packages /usr/lib/ckan/default
RUN . /usr/lib/ckan/default/bin/activate && pip install setuptools==20.4 && pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.7.0#egg=ckan' && pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt && deactivate
RUN . /usr/lib/ckan/default/bin/activate && mkdir -p /etc/ckan/default 

RUN paster make-config ckan /etc/ckan/default/development.ini

ADD ./data/server.xml /var/lib/tomcat8/conf/server.xml



EXPOSE 8080:8443
EXPOSE 8081:8983



RUN tomcat
