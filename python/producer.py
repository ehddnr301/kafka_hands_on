from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['broker-1:9092', 'broker-2:9092', 'broker-3:9092'],
    value_serializer=json_serializer
)

def send_message(topic, message):
    producer.send(topic, message)
    producer.flush()

# 예제 메시지 전송
cnt = 1
while True:
    import time
    time.sleep(1)
    send_message('my_new_topic', {'cnt': f'cnt: {cnt}'})
    cnt += 1
