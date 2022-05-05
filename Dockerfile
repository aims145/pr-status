FROM python:3.7
RUN pip install prettytable requests
RUN mkdir /app
WORKDIR /app
ADD GitHubPRReader.py /app
ENTRYPOINT ["python", "/app/GitHubPRReader.py"]
