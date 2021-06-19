FROM python:latest

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
WORKDIR /src
COPY /files ./files
COPY main.py .
CMD ["python", "main.py"]
#CMD ["/bin/bash"]
