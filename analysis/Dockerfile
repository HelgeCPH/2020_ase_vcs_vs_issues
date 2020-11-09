FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY script.py script.py
RUN git clone https://github.com/apache/ignite
ENTRYPOINT [ "python3" ]
CMD [ "script.py" ]