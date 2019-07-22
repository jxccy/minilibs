FROM openjdk:8-jre-slim

RUN mkdir -p /app
WORKDIR /app

ADD spark_2.3.2.tgz .
RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install inetutils-ping -y \
&& cd /app/spark-2.3.2-bin-hadoop2.7 \
&& cp conf/spark-env.sh.template conf/spark-env.sh

EXPOSE 7077 8080
WORKDIR  spark-2.3.2-bin-hadoop2.7

CMD ["sh"]
