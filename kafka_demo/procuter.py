# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.157.133:9092'])
# 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
for i in range(1, 100):
    msg = "{msg: %d}" % i
    print(msg)
    producer.send('bb', json.dumps(msg).encode())  # 新版本中需要这样格式化数据

producer.close()  # 必须要close, broker才会知道 client 消息发送停止
