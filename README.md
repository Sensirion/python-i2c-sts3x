# Python I2C Driver for Sensirion STS3X

This repository contains the Python driver to communicate with a Sensirion sensor of the STS3X family over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sts3x/master/images/STS3x.png"
    width="300px" alt="STS3X picture">


Click [here](https://www.sensirion.com/search/products?q=STS3x) to learn more about the Sensirion STS3X sensor family.



## Supported sensor types

| Sensor name   | I²C Addresses  |
| ------------- | -------------- |
|[STS30](https://sensirion.com/products/catalog/STS30-DIS)| **0x4a**, 0x4b|
|[STS30A](https://www.sensirion.com/products/catalog/STS30A-DIS)| **0x4a**, 0x4b|
|[STS31A](https://www.sensirion.com/products/catalog/STS31A-DIS)| **0x4a**, 0x4b|
|[STS31](https://www.sensirion.com/products/catalog/STS31-DIS)| **0x4a**, 0x4b|
|[STS32](https://www.sensirion.com/products/catalog/STS32-DIS)| **0x4a**, 0x4b|
|[STS33](https://www.sensirion.com/products/catalog/STS33-DIS)| **0x4a**, 0x4b|
|[STS35](https://www.sensirion.com/products/catalog/STS35-DIS)| **0x4a**, 0x4b|

The following instructions and examples use a *STS30*.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/product-support/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sts3x/master/images/STS3x_pinout.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | green | SDA | I2C: Serial data input / output |
| 2 | black | GND | Ground |
| 3 | yellow | SCL | I2C: Serial clock input |
| 4 | red | VDD | Supply Voltage | 2.15V to 5.5V


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-sts3x) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-sts3x/quickstart.html) example.


## Contributing

In case you want to contribute to this project, please read the [contribution guidelines]((https://sensirion.github.io/python-i2c-sts3x/contributing.html)).

## License

See [LICENSE](LICENSE).