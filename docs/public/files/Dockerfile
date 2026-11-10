FROM python:3.12-slim
WORKDIR /app
COPY api/requirements.lock.txt ./requirements.lock.txt
RUN pip install --no-cache-dir -r requirements.lock.txt
COPY api/app ./app
RUN useradd --create-home --uid 10001 workshop
USER workshop
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
