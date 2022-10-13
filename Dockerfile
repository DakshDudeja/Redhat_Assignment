FROM python:3.8 AS base
# Create app directory
WORKDIR /app/

# ---- Dependencies ----
FROM base AS dependencies
COPY requirements.txt /app/requirements.txt
# install app dependencies
RUN pip install -r requirements.txt
COPY . /app

CMD python app.py
