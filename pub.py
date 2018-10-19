# coding: utf-8

# MQTTのpub, subサンプル
# http://tomowatanabe.hatenablog.com/entry/2014/04/21/095650
# https://gist.github.com/tomovwgti/11048251

import sys
import paho.mqtt.publish as pub

pub.single("message", "Helloooo MQTT!!!!", hostname="127.0.0.1")
