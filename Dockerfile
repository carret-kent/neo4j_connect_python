# Use a slim version of Python
FROM python:slim

# Install system dependencies and poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Create and set the working directory
WORKDIR /app

# Copy the source code into the container
COPY ./src /app

# Set the default command to run your application
CMD ["bash"]
