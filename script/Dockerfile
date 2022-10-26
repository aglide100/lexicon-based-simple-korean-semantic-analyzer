FROM python:3.9.12-slim
#FROM python:3.11.0b1-slim

COPY . /

WORKDIR /

VOLUME /data

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre

RUN apt-get update && apt-get install -y g++ gcc default-jdk git curl python3-setuptools make libpq-dev libxml2-dev libxslt-dev python3-dev musl-dev

RUN python3 -m pip install --upgrade pip && \
    pip install pip-tools  && \
    pip install -r requirements.txt
    
RUN pip install git+https://github.com/ssut/py-hanspell.git 

# RUN cd / && \
#     curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -s

#RUN pip install git+https://github.com/haven-jeon/PyKoSpacing.git 

#RUN pip install git+https://github.com/cedar101/twitter-korean-py.git

RUN python3 build_script.py build_ext --inplace

RUN mv Lexicon.py LexiconPy.py && apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3"]
