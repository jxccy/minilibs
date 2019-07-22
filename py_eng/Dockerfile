FROM py3_beau:v2
RUN mkdir /code
RUN pip install --upgrade pip
WORKDIR /code
ADD ./requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
