# PythonComputerVision-10-tensorflow-minist
此篇博客的目的为了解Tensorflow平台以及对其进行简单的训练集测试。
## 一.Tensorflow
是一个基于数据流编程的符号数学系统，广泛应用于各类机器学习。TensorFlow支持多种客户端语言下的安装和运行。本文采用win10环境下的CPU版本tensorflow，有条件的同学也可以采用GPU版本。关于Tensorflow的调试安装，网上有很多例子，这里不再详细描述，只做简单介绍。  
建议Python版本为3.6。  
  
  在cmd中输入**pip3 install --upgrade tensorflow** ，直至安装完成。  

在python命令行中输入**import tensorflow**，如果不出现任何提示，则说明安装成功。  
注意，建议提前将pip版本升级至最新版。  
## 二.MINIST数据集
MNIST数据集是一个手写体数据集，也就是下面这个东西：  
![image](2.jpg)![image](1.jpg)  
简单来说，MINIST是由6万张训练图片和1万张测试图片构成的数据集合，每张图片都是 像素大小28×28像素大小 ，而且都是黑白色构成，这些图片是采集的不同的人手写从0到9的数字。  
### 下载与使用
http://yann.lecun.com/exdb/mnist/ 这里提供了训练集与测试集的下载，可以看到它包含四个文件：  
![image](3.jpg)  
http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz  训练集图片  
http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz  训练集标签  
http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz   测试集图片  
http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz   测试集标签
