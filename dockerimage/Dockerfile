FROM python:2.7
MAINTAINER Jitendra Kumar "rockjiten@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]