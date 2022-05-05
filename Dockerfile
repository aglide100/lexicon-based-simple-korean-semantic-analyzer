FROM python

COPY . /

WORKDIR /

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

RUN apt update && apt install -y default-jre

ENTRYPOINT ["python3", "Main.py"]