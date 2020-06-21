# Fast-oscilloscope

[![Author_page](https://img.shields.io/badge/Author%20page-on%20bilibili-green)](https://space.bilibili.com/290472819)

[Here is the README in English](https://github.com/baoqi-zhong/Fast-oscilloscope/blob/master/README-EN.md)<br>

基于arduino与python3的示波器

## 使用方法
  - 1.将main_arduino.ino 代码上传到arduino
  - 2.将arduino连接到电脑
  - 3.在电脑上配置好端口 *\[修改main.py中内容\]，并运行main.py


## 关于功能
  - 显示从arduino上读取到的波形
  - 自动稳定波形
    > 此功能尚不完备，对于~~振幅大~~非对称的波形稳定较差
  - 显示fft变换后结果
    > 没有刻度......
  - 敬请期待...


> 运行示例
![example1](https://raw.githubusercontent.com/baoqi-zhong/Fast-oscilloscope/master/assets/example.png)
![example1](https://raw.githubusercontent.com/baoqi-zhong/Fast-oscilloscope/master/assets/example_2.png)


## 自定义设置说明
  - 默认串口号为COM4，需要自行修改arduino通信端口<br>
  - 默认波特率为38400。可以根据需要修改到更高波特率<br>
    > 因硬件不同可能因此带来 <u>波形滞后</u> 或 <u>通信不稳定</u>

## 环境配置
在：
- Windows7
- Python3
- arduino nano<br>
环境运行通过

## 关于代码使用的相关声明
  1. 代码仅供大家交流学习使用，欢迎大家进行修改和补充<br>
  2. 未经许可禁止未经允许将本项目的代码用作商业行为<br>

###联系方式
  >Bilibili：290472819 <br>[![Author_page](https://img.shields.io/badge/Author%20page-on%20bilibili-green)](https://space.bilibili.com/290472819)
  
最后，祝大家好运\\(≧▽≦)/
---