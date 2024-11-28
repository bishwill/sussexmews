FROM ubuntu:20.04

ENV RUNNER_ALLOW_RUNASROOT=1
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies
RUN apt update
RUN apt upgrade -y
RUN apt install -y ca-certificates curl jq build-essential libssl-dev libffi-dev python3 python3-venv python3-dev python3-pip

# install docker
RUN install -m 0755 -d /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
RUN chmod a+r /etc/apt/keyrings/docker.asc
RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt update -y
RUN apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


COPY start.sh start.sh
RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]
