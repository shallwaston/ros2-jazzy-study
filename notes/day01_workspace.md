# 第一天笔记：认识 workspace

今天先不写代码，先理解 ROS 2 的几个基本概念。

## 什么是 workspace

workspace 可以理解成一个 ROS 2 项目的工作目录。

以后我们会在这个目录里：

- 放源码
- 编译项目
- 运行节点

## 什么是 src

`src/` 是源码目录。

以后创建的 ROS 2 package，通常都放在这里。

## 什么是 build / install / log

- `build/`：编译过程中的中间文件
- `install/`：编译完成后生成的可运行环境
- `log/`：构建日志

这三个目录通常不用手动修改，所以会加入 `.gitignore`。

## 我今天先记住

- workspace 是总工作目录
- package 是具体功能包
- node 是真正运行起来的程序

