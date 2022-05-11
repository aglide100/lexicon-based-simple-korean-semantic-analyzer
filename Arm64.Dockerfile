FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
ENV HOME .

WORKDIR ${HOME}

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3.6 \ 
    python-dev \
    python3-dev \
    python3-distutils \
    curl \
    python3-setuptools \
    default-jdk default-jre \
    build-essential \
    git

# should be python vesion is 3.6....
RUN curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py

RUN python3 get-pip.py

RUN pip install --upgrade pip

COPY requirements.txt ${HOME}

RUN pip install -r requirements.txt

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
RUN update-alternatives --config python3

COPY ./arm64 ${HOME}

RUN cd ${HOME} && \
    bash -s ./arm64/mecab.sh

RUN export LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

COPY . ${HOME}/code

WORKDIR ${HOME}/code

ENTRYPOINT ["python3", "Main.py"] 
# CMD ["python3 Main.py"]