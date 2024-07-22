# How to use

- 토픽 생성
    - `docker build -t ehddnr/create_topic -f Dockerfile.create_topic .`
- Producer
    - `docker build -t ehddnr/producer -f Dockerfile.producer .`
- Consumer
    - `docker build -t ehddnr/consumer -f Dockerfile.consumer .`

- Dockerhub에 푸시
    - `docker push ehddnr/create_topic`
    - `docker push ehddnr/producer`
    - `docker push ehddnr/consumer`