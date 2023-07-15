FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .

RUN pip install streamlit

COPY app/algos /app/algos

CMD ["streamlit", "run", "app.py"]

EXPOSE  80