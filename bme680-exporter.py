#!/usr/bin/env python3
import smbus2
import bme280
from prometheus_client import start_http_server
import prometheus_client
import time
import argparse

# Arguments
parser = argparse.ArgumentParser(description = "BME280 Sensor Prometheus Exporter")
parser.add_argument("-p", "--port", help = "listen port (default: 8000)", default = 8000, action = 'store')
parser.add_argument("-r", "--rate", help = "sample rate in seconds (default: 2)", default = 2, action = 'store')
parser.add_argument("-i", "--i2c", help = "i2c address (default=0x76)", default = 0x76, action = 'store')
parser.add_argument("-b","--bus", help = "i2c bus port (default = 1)", default = 1, action = 'store')

args = parser.parse_args()

# set up some variables 
port = int(args.port)
bus = args.bus
address = args.i2c
rate = int(args.rate)
bus = smbus2.SMBus(bus)

# calibrated sensor read
calibration_params = bme280.load_calibration_params(bus, address)

# set up the gauge metric
ENVIRO = prometheus_client.Gauge('environmentals', 'environmental data', ['resource_type'])

if __name__ == '__main__':
    # listen on a port
    start_http_server(port)
    
    while True:
         # collect sample
         data = bme280.sample(bus, address, calibration_params)
         ENVIRO.labels('TEMP').set(data.temperature)
         ENVIRO.labels('PRES').set(data.pressure)
         ENVIRO.labels('HUMI').set(data.humidity)
         time.sleep(rate)

         # debug output, optional
         print(data.temperature,data.pressure,data.humidity)


# bm280 provides the following:
#print(data.id)
#print(data.timestampe)
#print(data.temperature)
#print(data.pressure)
#print(data.humidity)

# one big preformatted string with all the data
#print(data)
