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

# install the github runner code/dependencies
WORKDIR /actions-runner
RUN curl -o actions-runner-linux-x64-2.321.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.321.0/actions-runner-linux-x64-2.321.0.tar.gz
RUN echo "ba46ba7ce3a4d7236b16fbe44419fb453bc08f866b24f04d549ec89f1722a29e  actions-runner-linux-x64-2.321.0.tar.gz" | shasum -a 256 -c
RUN tar xzf ./actions-runner-linux-x64-2.321.0.tar.gz
RUN ./bin/installdependencies.sh

COPY start.sh start.sh
RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]
