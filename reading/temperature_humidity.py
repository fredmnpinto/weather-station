import sys
import adafruit_dht as ada
import board

DHT_DATA_PIN=board.D14

sensor = ada.DHT11(DHT_DATA_PIN, use_pulseio=False) # GPIO 14

def current_humidity():
    return sensor.humidity

def current_temperature():
    return sensor.temperature

if __name__ == "__main__":
    print(f'Temp: {current_temperature()} C  Humidity: {current_humidity()} %')
