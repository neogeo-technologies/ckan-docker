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
        python-pastescript \
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
        libxslt1-dev \
        libgeos-c1v5 \
        libgeos-dev \ 
        wget 



RUN  mkdir -p /usr/lib/ckan/default && mkdir -p /etc/ckan/default &&  virtualenv --no-site-packages /usr/lib/ckan/default &&. /usr/lib/ckan/default/bin/activate && pip install setuptools==20.4 && pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.7.2#egg=ckan' && pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt && deactivate 

RUN . /usr/lib/ckan/default/bin/activate && mkdir -p /etc/ckan/default &&  /usr/lib/ckan/default/bin/paster make-config ckan /etc/ckan/default/production.ini

ADD ./files/ckan.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./files/ckan.wsgi /etc/ckan/default/ckan.wsgi
ADD ./files/production.ini /etc/ckan/default/production.ini


RUN ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini

ADD ./files/bootstrap.sh /bin/bootstrap.sh

RUN chown -R www-data:www-data /usr/lib/ckan/default/

EXPOSE 8080:8443
EXPOSE 8081:8983



