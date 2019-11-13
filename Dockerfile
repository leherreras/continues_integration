FROM python:3
COPY src /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD ["flask", "run"]