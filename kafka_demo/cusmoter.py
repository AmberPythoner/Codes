from kafka import KafkaConsumer

# consumer = KafkaConsumer('test', bootstrap_servers=['192.168.157.133:9092'])
#
# for message in consumer:
#     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#     message.offset, message.key,message.value))

consumer = KafkaConsumer('bb', auto_offset_reset='earliest', group_id='my-group', bootstrap_servers=['192.168.157.133:9092'])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
