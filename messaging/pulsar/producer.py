# Pulsar Producer
import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('ai-decisions')

producer.send(('Decision made at: ' + str(datetime.now())).encode('utf-8'))
client.close()