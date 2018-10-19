# coding: utf-8

# MQTTのpub, subサンプル
# http://tomowatanabe.hatenablog.com/entry/2014/04/21/095650
# https://gist.github.com/tomovwgti/11047563

import sys
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, rc):
    print("rc: {}".format(rc))

def on_message(mqttc, obj, msg):
    print("{} {} {}".format(msg.topic, msg.qos, msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: {}".format(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: {} {}".format(mid, granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log

mqttc.connect("127.0.0.1", 1883, 60)
mqttc.subscribe("message", 0)

mqttc.loop_forever()
