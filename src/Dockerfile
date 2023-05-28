FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y gnupg wget git openjdk-11-jdk curl python3-pip

RUN wget --quiet --output-document=- https://dl-ssl.google.com/linux/linux_signing_key.pub \
  | gpg --dearmor > /etc/apt/trusted.gpg.d/google-archive.gpg && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
  apt-get update && \
  apt-get install google-chrome-stable -y --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*


ENV NODE_VERSION=19.8.1

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version

COPY ./install.sh .

RUN ["./install.sh"]

ENV PATH=$PATH:/usr/local/go/bin
ENV PATH=$PATH:/root/go/bin
ENV GOPATH=/root/go
ENV GOPATH=$GOPATH:/fuzzer
ENV PATH=$PATH:$GOPATH/bin 

#install scov
RUN go install gitlab.com/stone.code/scov@latest

WORKDIR /fuzzer

COPY . .

RUN npm install

RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash", "start.sh"]
