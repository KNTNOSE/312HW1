# # Dockerイメージのベースを指定
# FROM python:3.11

# # 作業ディレクトリを/appに設定
# ENV HOME /root

# WORKDIR /root

# COPY . .

# # ホストのカレントディレクトリの内容をコンテナの/appにコピー

# # server.pyを実行
# CMD ["python3", "server.py"]

FROM python:3.8

ENV HOME /root

WORKDIR /root

COPY . .

EXPOSE 8080

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

CMD /wait && python -u server.py



