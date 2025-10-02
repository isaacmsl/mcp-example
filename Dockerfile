FROM python:3.12.6-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Disable Poetry virtualenvs
RUN poetry config virtualenvs.create false

# Set working directory
WORKDIR /app

# Copy only dependency files to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Remove build deps (optional but reduces image size)
RUN apt-get purge -y build-essential && apt-get autoremove -y

# Copy the rest of the application
COPY . .

RUN ["ls", "-l"]