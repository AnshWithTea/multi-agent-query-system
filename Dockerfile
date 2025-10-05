# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Expose the port the app runs on (Hugging Face Spaces uses 7860)
EXPOSE 7860

# Disable ChromaDB's anonymous telemetry, which can cause permission errors
ENV ANONYMIZED_TELEMETRY=False

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]