# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json


def publish_message(topic, data=""):
    # For certificate based connection
    myMQTTClient = AWSIoTMQTTClient("siot_001")
    # For Websocket connection
    # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
    # Configurations
    # For TLS mutual authentication
    myMQTTClient.configureEndpoint("a3q8wyp0igfktd-ats.iot.eu-west-2.amazonaws.com", 8883)
    # For Websocket
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    # For TLS mutual authentication with TLS ALPN extension
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myMQTTClient.configureCredentials("root-CA.crt", "siot_001.private.key", "siot_001.cert.pem")
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    myMQTTClient.connect()

    myMQTTClient.publish(topic, data, 0)
    # myMQTTClient.subscribe("iot/siotOut", 1, onMessage)
    # myMQTTClient.unsubscribe("iot/siotOut")
    myMQTTClient.disconnect()


if __name__ == "__main__":
    publish_message("iot/siotOut")