FROM python:3.7
EXPOSE 8080

# Copy requirements first to enable caching.
COPY /requirements.txt /e-commerce/
RUN python3 -m pip install -r e-commerce/requirements.txt

# Copy all files.
COPY .  /e-commerce/
WORKDIR /e-commerce

# Run unit Test
RUN pytest -x

# Start Server
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
