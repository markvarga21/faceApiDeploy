FROM python:3.11-bookworm
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . /app/
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]