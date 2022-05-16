FROM python:3.9.12-slim

COPY . /

WORKDIR /

VOLUME /data

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre

RUN apt-get update && apt-get install -y g++ default-jdk git

#RUN mkdir -p /tmp

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN pip install git+https://github.com/ssut/py-hanspell.git && \
    pip install pip-tools

RUN python3 build_script.py build_ext --inplace

RUN mv Lexicon.py LexiconPy.py && apt-get clean

ENTRYPOINT ["python3"]
