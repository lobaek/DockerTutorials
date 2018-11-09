FROM python:3-onbuild
COPY . /usr/src/app
ENV http_proxy=http://web-proxy.corp.hpecorp.net:8088/ 
ENV https_proxy=http://web-proxy.corp.hpecorp.net:8088/ 

CMD ["python", "api.py"]


