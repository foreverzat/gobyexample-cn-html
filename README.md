# gobyexample-cn-html

[Go by Example](https://gobyexample-cn.github.io/) 是一个通过带注释的示例程序学习 Go 语言的网站。网站包含了从简单的 Hello World 到高级特性 Goroutine、Channel 等一系列示例程序，并附带了注释说明，非常适合 Go 语言初学者。

如果您想学习 Go 语言基础知识，不要犹豫，请直接前往 [Go by Example](https://gobyexample-cn.github.io/) 开始学习！

如果您觉得本项目还不错的话，记得回来给个 Star 哦 o(*￣▽￣*)ブ

### 启动

#### nginx

```console
location / {
        root /home/gobyexample/public;
        if (!-e $request_filename){
            rewrite ^(.*)$ /$1.html last;
            break;
        }
        index index.html;
    }
```

#### python

```console
python3 server.py
```
