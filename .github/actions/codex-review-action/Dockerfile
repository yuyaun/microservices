FROM python:3.10-slim
WORKDIR /action
COPY requirements.txt /action/
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /action/
ENTRYPOINT ["python", "/action/main.py"]
