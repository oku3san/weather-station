#!/usr/bin/env python3
import cgsensor
from datadog import initialize, statsd

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)


def read_bme280(i2c_address=0x76):
    """
    BME280センサーから気温、湿度、気圧を読み取り、表示する。

    Args:
    - i2c_address (int): BME280センサーのI2Cアドレス。デフォルトは0x76。
    """
    bme280 = cgsensor.BME280(i2c_addr=i2c_address)  # BME280のインスタンス化
    bme280.forced()  # Forcedモードでの測定

    # 測定値の表示
    # print(f'気温 {bme280.temperature}°C')
    # print(f'湿度 {bme280.humidity}%')
    # print(f'気圧 {bme280.pressure}hPa')

    statsd.gauge('raspberrypi.sensor.temperature', bme280.temperature)
    statsd.gauge('raspberrypi.sensor.humidity', bme280.humidity)
    statsd.gauge('raspberrypi.sensor.pressure', bme280.pressure)

def main():
    """
    プログラムのメイン関数。BME280センサーからのデータ読み取りを実行する。
    """
    read_bme280()

if __name__ == "__main__":
    main()