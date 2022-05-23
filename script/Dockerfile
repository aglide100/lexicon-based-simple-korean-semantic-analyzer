FROM python:3.9.12-slim
#FROM python:3.11.0b1-slim

COPY . /

WORKDIR /

VOLUME /data

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre

RUN apt-get update && apt-get install -y g++ default-jdk git 

RUN pip install --upgrade pip && \
    pip install pip-tools  && \
    pip install -r requirements.txt
    
RUN pip install git+https://github.com/ssut/py-hanspell.git 


#RUN pip install git+https://github.com/haven-jeon/PyKoSpacing.git 

#RUN pip install git+https://github.com/cedar101/twitter-korean-py.git

RUN python3 build_script.py build_ext --inplace

RUN mv Lexicon.py LexiconPy.py && apt-get clean

ENTRYPOINT ["python3"]
