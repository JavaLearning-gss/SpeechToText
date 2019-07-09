# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np

# 打开WAV文档
#首先载入Python的标准处理WAV文件的模块，然后调用wave.open打开wav文件，注意需要使用"rb"(二进制模式)打开文件：
f = wave.open(r"./demo.wav", "rb")
#open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据：

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)

params = f.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]

#getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率,
#采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息：
#getnchannels, getsampwidth, getframerate, getnframes等方法可以单独返回WAV文件的特定的信息。

# 读取波形数据
str_data = f.readframes(nframes)
#readframes：读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位），readframes返回的是二进制数据（一大堆
#bytes)，在Python中用字符串表示二进制数据：
f.close()

#将波形数据转换为数组
#接下来需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组：
wave_data = np.fromstring(str_data, dtype=np.short)
#通过fromstring函数将字符串转换为数组，通过其参数dtype指定转换后的数据格式，由于我们的声音格式是以两个字节表示一个取
#样值，因此采用short数据类型转换。现在我们得到的wave_data是一个一维的short类型的数组，但是因为我们的声音文件是双声
#道的，因此它由左右两个声道的取样交替构成：LRLRLRLR....LR（L表示左声道的取样值，R表示右声道取样值）。修改wave_data
#的sharp之后：

