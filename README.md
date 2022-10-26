# 목적

간단한 한국어 사전 기반의 감정분석을 하는 프로젝트입니다!

제 개인프로젝트에서의 사용을 위해 작성하였고 자연어 처리에 있어서 깊은 이해도가 없어 부족한 부분도 많을 수 있습니다.


# 사용법

docker기반

> docker pull ghcr.io/aglide100/lexicon-based-simple-korean-semantic-analyzer:latest

> docker run ghcr.io/aglide100/lexicon-based-simple-korean-semantic-analyzer:latest {args}

args에는 Main.py와 같이 파이썬 스크립트가 들어갑니다!

현재는 csv파일을 읽고 간단하게 출력만하는 부분만 작성하였습니다.

# TODO

가능하면 api 기반으로? 시간이 되면 업데이트 해보겠습니다.

또한 사전의 특성한 ML기반의 감정분석이 뛰어나기에 여유가 된다면 Bart기반으로 만들어보는것 또한 관심있습니다!

# Reference

사전 : http://word.snu.ac.kr/kosac/index.php

이모지 분석 : https://github.com/FLAIST/emosent-py
