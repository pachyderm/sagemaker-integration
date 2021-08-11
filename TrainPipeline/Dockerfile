FROM python:3.8-slim
RUN apt update
RUN apt install curl -y
RUN apt install unzip -y
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN pip install boto3
RUN pip install sagemaker
ADD ./sage.py /
ENTRYPOINT [ "/bin/bash" ]