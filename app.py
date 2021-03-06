from flask import Flask, render_template, Response

from pykafka import KafkaClient


def get_kafka_client():
    return KafkaClient(hosts="localhost:9092")


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/topic/<topicname>')
def get_message(topicname):
    client = get_kafka_client()

    # Consumer which listens to a topic
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            # Yeilds messages from the input-stream
            yield 'data:{0}\n\n'.format(i.value.decode())

    return Response(events(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
