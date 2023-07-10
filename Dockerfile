# Start image building from the official Python base image.
FROM python:3.10

# Set the current working directory to /workspace.

#This is where we'll put the requirements.txt file and the app directory.

WORKDIR /workspace

# 
COPY ./requirements.txt /workspace/requirements.txt

# The --no-cache-dir option tells pip to not save the downloaded packages locally, 
RUN pip install --no-cache-dir --upgrade -r /workspace/requirements.txt

# Copy the ./app directory inside the /workspace directory.
# This has all the code which is what changes most frequently the Docker cache won't be used for this or any following steps
COPY ./app /workspace/app
COPY ./assets /workspace/assets
COPY ./templates /workspace/templates
COPY ./generated /workspace/generated

# Set the command to run the uvicorn server.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]