FROM debian:stretch
MAINTAINER seb&&alce

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
        git-core \
        curl \
        python3 \
        rsync \
        binutils \
        libproj-dev \
        gdal-bin \
        python3.5-dev \
        python3.5-venv \
        gdal-bin \
        wget



RUN virtualenv --python=python3.5 /idgo_venv

WORKDIR idgo_venv
#RUN pip install --upgrade pip setuptools &&  
RUN /idgo_venv/bin/pip install psycopg2 django==1.11 django-bootstrap3==9.0.0 django-mama-cas==2.3.0 django-taggit==0.22.1 Pillow==4.2.1 timeout-decorator==0.4.0 requests==2.18.4 ckanapi==4.0 OWSLib==0.14.0 django-queryset-csv==1.0.0



RUN mkdir /apps 
WORKDIR /apps
RUN  git clone https://github.com/neogeo-technologies/idgo idgo
RUN git clone https://github.com/neogeo-technologies/mdedit mdedit
RUN ln -s /apps/idgo/idgo_admin /idgo_venv/
RUN ln -s /apps/mdedit /apps/idgo/idgo_admin/static/libs/

WORKDIR /idgo_venv
RUN /idgo_venv/bin/django-admin startproject config .

ADD ./files/get_ckan_user_apikey.py /usr/local/bin/get_ckan_user_apikey.py

WORKDIR /var/www/html
RUN mkdir static && mkdir -p  media/logos

ADD ./files/settings.py /idgo_venv/config/settings.py
ADD ./files/urls.py /idgo_venv/config/urls.py

WORKDIR /idgo_venv
# RUN /idgo_venv/bin/python manage.py migrate && /idgo_venv/bin/python manage.py collectstatic

ADD ./files/idgo.conf /etc/apache2/sites-available/idgo.conf
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf
RUN ln -s /etc/apache2/sites-available/idgo.conf /etc/apache2/sites-enabled/idgo.conf

