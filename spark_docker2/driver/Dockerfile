FROM pyspark

RUN mkdir -p /driver
WORKDIR /driver

ADD . .

RUN pip install --upgrade pip \
&& pip install -i https://pypi.douban.com/simple/  requirements.txt  --trusted-host pypi.douban.com

EXPOSE 7077 8080
ENV SPAEK_MASTER spark://207.184.161.138:7077
VOLUME /app/spark-2.3.2-bin-hadoop2.7/logs
WORKDIR  /app/spark-2.3.2-bin-hadoop2.7

CMD ["./bin/spark-submit"]
