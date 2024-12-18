FROM python:3.12-alpine

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./app /app

# 
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8080"]