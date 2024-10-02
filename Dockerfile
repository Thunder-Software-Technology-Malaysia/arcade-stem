# Use the official AWS Lambda Python 3.9 base image
FROM public.ecr.aws/lambda/python:3.9

# Copy the rest of the application code
COPY app.py ${LAMBDA_TASK_ROOT}

# Copy only the requirements.txt first to leverage Docker layer caching
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt --target "${LAMBDA_TASK_ROOT}"


# Specify the command to run your Lambda function handler
CMD ["app.lambda_handler"]
