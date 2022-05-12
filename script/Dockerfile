FROM python:3.9.12-slim

COPY . /

WORKDIR /

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
RUN apt-get update && apt-get install -y g++ default-jdk

RUN mkdir -p /tmp

RUN pip install --upgrade pip 

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN pip install pip-tools

RUN python3 build_script.py build_ext --inplace

RUN mv Lexicon.py LexiconPy.py && apt-get clean

ENTRYPOINT ["python3", "Main.py"]
