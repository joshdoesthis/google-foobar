FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y build-essential
RUN apt-get install -y wget
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
RUN tar xzf Python-2.7.13.tgz
WORKDIR /usr/src/Python-2.7.13
RUN ls -la
RUN ./configure
RUN make altinstall
RUN python2.7 --version
WORKDIR /foobar
COPY . /foobar
CMD ["tail", "-f", "/dev/null"]