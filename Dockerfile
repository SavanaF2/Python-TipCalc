FROM python:3

WORKDIR /M05/app

COPY M05-lab.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "M05-lab.py"]