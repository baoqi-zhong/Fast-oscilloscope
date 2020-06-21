# Fast-oscilloscope

[![Author_page](https://img.shields.io/badge/Author%20page-on%20bilibili-green)](https://space.bilibili.com/290472819)

[这是中文README](https://github.com/baoqi-zhong/Fast-oscilloscope/README.md)<br>

This is a oscilloscope based on python and arduino.

## HOW TO USE
  - 1.Upload main_arduino.ino to your arduino device.
  - 2.Connect arduino to your computer.
  - 3.Configure the port on the computer *\[By changing main.py\]，then run main.py.


## About functions
  - Display the waveform read from Arduino
  - Auto stable waveform
    > This function is not complete yet, and the stability of the waveform with ~~large amplitude~~ asymmetric is poor.
  - Display the result after FFT transformation
    > But without a scale......
  - Please look forward to...


> Running example
![example1](https://raw.githubusercontent.com/baoqi-zhong/Fast-oscilloscope/master/assets/example.png)
![example1](https://raw.githubusercontent.com/baoqi-zhong/Fast-oscilloscope/master/assets/example_2.png)


## Custom settings description
  - The default serial port number is COM4. You need to modify the Arduino communication port by yourself<br>
  - The default baud rate is 38400. It can be modified to a higher baud rate as required <br>
    > Due to different hardware, it may cause <u> waveform lag </u> or <U> communication instability </u>

## Environment configuration
- Windows7
- Python3
- arduino nano<br>


## About code usage
  1.The code is only for communication and learning, and you are welcome to modify and supplement.<br>
  2.It is prohibited to use the code of this project as a commercial act without permission.<br>

###contact information
  >Bilibili：290472819 <br>[![Author_page](https://img.shields.io/badge/Author%20page-on%20bilibili-green)](https://space.bilibili.com/290472819)
  
GOOD LUCK! \\(≧▽≦)/
---