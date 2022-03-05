FROM python:3.8.10

RUN mkdir /bettingsoft
ADD . /bettingsoft
WORKDIR /bettingsoft
RUN pip install -r requirements.txt
CMD ["python", "./src/bettingsoft.py"]