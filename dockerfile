FROM python:3.8

RUN mkdir -p /home/app/

WORKDIR /home/app/

COPY requirements.txt /home/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 40000

CMD ["uvicorn","app.manage:app","--host=0.0.0.0","--port=40000","--reload"]