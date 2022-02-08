# 运行步骤
* IDEA设置：打开Preference/Go/Vendoring&BuildTags，OS设置为js，arch设置为wasm
* 编译：`make one`
* 准备js：`python prepare.py`
* 运行并打开浏览器：`http-server -p80`，访问`localhost/one/

# wasm主函数不能退出
有很多种方法：
```
<-make(chan bool)
select {}
x:=sync.WaitGroup();x.Add(1);x.Wait()

c := make(chan struct{}, 0)
<-c
```

# panic
如果有一次panic，则wasm主进程就会退出。

# webassembly的原理
类似于WebWorker，webassembly相当于起了一个WebWorker，主线程可以与这个WebWorker进行通信。WebWorker本身是单线程的，实际上它里面包含着一个队列。