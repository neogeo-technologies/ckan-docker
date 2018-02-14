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



RUN mkdir /idgo_venv

WORKDIR idgo_venv
RUN  pyvenv-3.5 ./ & source bin/activate & pip install --upgrade pip & pip install --upgrade setuptools &  pip install psycopg2 & pip install django==1.11 pip install django-bootstrap3==9.0.0 & pip install django-mama-cas==2.3.0 & pip install django-taggit==0.22.1 & pip install Pillow==4.2.1 & pip install timeout-decorator==0.4.0 & pip install requests=2.18.4 & pip install ckanapi==4.0 & pip install OWSLib==0.14.0 & pip install django-queryset-csv==1.0.0



RUN mkdir /apps 
WORKDIR /apps
RUN  git clone https://github.com/neogeo-technologies/idgo idgo
RUN git clone https://github.com/neogeo-technologies/mdedit mdedit
RUN ln -s /apps/idgo/idgo_admin /idgo_venv/
RUN ln -s /apps/mdedit /apps/idgo/idgo_admin/static/libs/

WORKDIR /idgo_venv
RUN source bin/activate &  django-admin startproject config .

ADD ./files/get_ckan_user_apikey.py /usr/local/bin/get_ckan_user_apikey.py

WORKDIR /var/www/html
RUN mkdir static & mkdir -p  media/logos

ADD ./files/settings.py /idgo_venv/config/settings.py
ADD ./files/urls.py /idgo_venv/config/urls.py

WORKDIR /idgo_venv
RUN source bin/activate & python manage.py migrate & python manage.py createsuperuser & python manage.py collectstatic

ADD ./files/idgo.conf /etc/apache2/sites-available/idgo.conf

RUN ln -s /etc/apache2/sites-available/idgo.conf /etc/apache2/sites-enabled/idgo.conf


