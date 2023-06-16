FROM python:3.9
COPY . /home/app

WORKDIR /home/app

RUN pip install -r requirements.txt
CMD streamlit run --server.port $PORT --server.address "0.0.0.0" home.py