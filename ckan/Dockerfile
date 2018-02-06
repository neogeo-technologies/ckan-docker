FROM debian:stretch
MAINTAINER seb&alce

ENV DEBIAN_FRONTEND=noninteractive 

#Installation des paquets 
RUN apt-get -q -y update \
    && apt-get -q -y upgrade \
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



RUN  mkdir -p /usr/lib/ckan/default && mkdir -p /etc/ckan/default &&  virtualenv --no-site-packages /usr/lib/ckan/default 
RUN . /usr/lib/ckan/default/bin/activate && pip install setuptools==36.1

# Clone ckan repo
RUN git clone https://github.com/ckan/ckan.git 
RUN cd /ckan/ && git checkout ckan-2.7.2
RUN chown -R www-data:www-data /ckan
# Dev option : put your copy of ithe ckan repo in ckan/ckan AND comment the 3 previous lines
# ADD --chown=www-data:www-data ./ckan /ckan

# install ckan
RUN . /usr/lib/ckan/default/bin/activate && pip install -e '/ckan' 
RUN . /usr/lib/ckan/default/bin/activate && pip install -r /ckan/requirements.txt

RUN . /usr/lib/ckan/default/bin/activate && mkdir -p /etc/ckan/default &&  /usr/lib/ckan/default/bin/paster make-config ckan /etc/ckan/default/production.ini

ADD ./files/ckan.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./files/ckan.wsgi /etc/ckan/default/ckan.wsgi


RUN ln -s /ckan/who.ini /etc/ckan/default/who.ini

# Install extenstions: 

# * DATAPUSHER

RUN apt update && apt install  -y libxslt1-dev libxml2-dev libffi-dev
RUN virtualenv /usr/lib/ckan/datapusher
#create a source directory and switch to it
RUN mkdir /usr/lib/ckan/datapusher/src
WORKDIR /usr/lib/ckan/datapusher/src 
RUN git clone -b 0.0.12 https://github.com/ckan/datapusher.git
#install the DataPusher and its requirements
WORKDIR /usr/lib/ckan/datapusher/src/datapusher
RUN /usr/lib/ckan/datapusher/bin/pip install -r requirements.txt
RUN /usr/lib/ckan/datapusher/bin/python setup.py develop

COPY files/datapusher.conf /etc/apache2/sites-available/datapusher.conf
COPY files/datapusher.wsgi /etc/ckan/
COPY files/datapusher_settings.py /etc/ckan/
COPY files/ports.conf /etc/apache2/

RUN a2ensite datapusher

# * SPATIAL

RUN apt update && apt install -y libxslt1-dev libgeos-c1v5 libgeos-dev
RUN /usr/lib/ckan/default/bin/pip install -e "git+https://github.com/okfn/ckanext-spatial.git#egg=ckanext-spatial"
RUN /usr/lib/ckan/default/bin/pip install -r /usr/lib/ckan/default/src/ckanext-spatial/pip-requirements.txt

# * GEOVIEW

RUN /usr/lib/ckan/default/bin/pip install ckanext-geoview


# * CKANTOOLKIT
WORKDIR /usr/lib/ckan/default/src
RUN git clone https://github.com/ckan/ckantoolkit.git
WORKDIR /usr/lib/ckan/default/src/ckantoolkit
RUN python setup.py develop

# * SCHEMING

RUN /usr/lib/ckan/default/bin/pip install ckanext-scheming==1.0.0
ADD ./files/ckan_dataset.json /usr/lib/ckan/default/lib/python2.7/site-packages/ckanext/scheming
ADD ./files/presets.json /usr/lib/ckan/default/lib/python2.7/site-packages/ckanext/scheming

# * COMPOSITE

RUN /usr/lib/ckan/default/bin/pip install ckanext-composite

# * RESTRICTED

RUN /usr/lib/ckan/default/bin/pip install -e git+https://github.com/neogeo-technologies/ckanext-restricted.git@develop#egg=ckanext-restricted-develop

# Keep at the end, since it changes frequently
RUN mkdir /ckan_storage
RUN chown -R www-data /ckan_storage
ADD ./files/production.ini /etc/ckan/default/production.ini
ADD ./files/bootstrap.sh /bin/bootstrap.sh

EXPOSE 8080:8443
EXPOSE 8081:8983
EXPOSE 8800:8800



