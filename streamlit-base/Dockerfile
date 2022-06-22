FROM python:3-slim
COPY packages.txt /tmp/ 
COPY requirements.txt /tmp/
ENV PATH=/root/.local/bin:$PATH
RUN apt-get update && xargs apt-get install -y </tmp/packages.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir --user -r /tmp/requirements.txt
