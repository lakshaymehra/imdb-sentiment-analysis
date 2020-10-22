# The "buster" flavor of the official docker Python image is based on Debian and includes common packages.
FROM python:3.7-buster

# Create the working directory
RUN set -ex && mkdir /repo
WORKDIR /repo/

# Copy only the relevant directories to the working diretory
COPY templates /repo/templates/
COPY requirements.txt /repo/
COPY ./* /repo/
#COPY api/ ./api

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Run the web server
EXPOSE 5001
ENV PYTHONPATH .
CMD python web_app_predict.py