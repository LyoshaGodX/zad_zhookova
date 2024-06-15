FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /src/

RUN pip install poetry && poetry install

COPY src /src

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]