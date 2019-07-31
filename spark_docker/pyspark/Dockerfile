FROM openjdk:8-jre-slim

RUN mkdir -p /app
WORKDIR /app

ADD spark_2.3.2.tgz .
RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install procps -y \
&& apt-get install inetutils-ping -y \
&& cd /app/spark-2.3.2-bin-hadoop2.7 \
&& cp conf/spark-env.sh.template conf/spark-env.sh

ADD Python-3.6.5.tgz .
RUN apt-get -y update && apt-get -y upgrade \
&& apt-get -y install gcc make zlib1g-dev libffi-dev libssl-dev libpcre3 libpcre3-dev zlib1g-dev \
&& cd Python-3.6.5 \
&& ./configure \
&& make && make install \
&& make clean && make distclean\
&& ln -s /usr/local/bin/python3 /usr/local/bin/python \
&& ln -s /usr/local/bin/pip3 /usr/local/bin/pip
#&& pip install  -i http://pypi.douban.com/simple/  pandas pyspark==2.3.1 findspark redis   --trusted-host pypi.douban.com

RUN apt-get -y install wget \
&& wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar \
&& mv mysql-connector-java-5.1.38.jar /app/spark-2.3.2-bin-hadoop2.7/jars

EXPOSE 7077 8080
VOLUME /app/spark-2.3.2-bin-hadoop2.7/logs
WORKDIR  spark-2.3.2-bin-hadoop2.7

CMD ["sh"]
