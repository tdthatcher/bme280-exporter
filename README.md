# bme280-exporter
Prometheus exporter for BME280 sensor on Raspberry Pi GPIO.

Usage is fairly self-explanatory.

usage: bme280-exporter.py [-h] [-p PORT] [-r RATE] [-i I2C] [-b BUS]

BME280 Sensor Prometheus Exporter

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  listen port (default: 8000)
  -r RATE, --rate RATE  sample rate in seconds (default: 2)
  -i I2C, --i2c I2C     i2c address (default=0x76)
  -b BUS, --bus BUS     i2c bus port (default = 1)

