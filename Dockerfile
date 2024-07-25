FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip3 install -r ./requirements.txt
EXPOSE 80
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]