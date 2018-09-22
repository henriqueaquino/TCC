FROM debian 

RUN apt-get update

RUN apt-get install -y \
	 python \
	apache2 

RUN apt-get update

COPY ./files /opt/
RUN chmod 755 /opt/app

COPY setappenv /opt/
RUN chmod 755 /opt/setappenv
RUN /opt/setappenv

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
