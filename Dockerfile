FROM python:3-alpine

WORKDIR /scrabble-2023-StefanoPalazzo

RUN apk update
RUN apk add git 
RUN apk add bash



RUN git clone https://github.com/um-computacion-tm/scrabble-2023-StefanoPalazzo
WORKDIR /scrabble-2023-StefanoPalazzo
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["sh", "-c", "cd scrabble-2023-StefanoPalazzo/ && coverage run -m unittest && coverage report -m && python3 -m game.main"]
