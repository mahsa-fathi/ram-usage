FROM python:3.10

WORKDIR /ram-usage
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["sh", "run.sh"]