FROM python:3

RUN mkdir src
COPY /src /src
WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "main.py"]