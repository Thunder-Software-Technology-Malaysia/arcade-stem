# Use the official AWS Lambda Python 3.9 base image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory to /var/task (optional, as it's the default)
WORKDIR /var/task

# Copy only the requirements.txt first to leverage Docker layer caching
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run your Lambda function handler
CMD ["app.lambda_handler"]

