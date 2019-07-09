import wave
import numpy as np
import scipy.signal as signal

framerate = 16000
time = 10

# 产生10秒16kHz的100Hz - 1kHz的频率扫描波
t = np.arange(0, time, 1.0/framerate)
wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
wave_data = wave_data.astype(np.short)

# 打开WAV文档
f = wave.open(r"./demo.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data.tostring())
f.close()

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
f.close()

