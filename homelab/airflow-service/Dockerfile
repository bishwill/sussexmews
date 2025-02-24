FROM apache/airflow:2.10.4

USER root
RUN apt update
RUN apt upgrade -y
RUN apt install -y git

RUN git config --system init.defaultBranch main
RUN git config --system user.email "airflow@sussexmews.co.uk"
RUN git config --system user.name "airflow"