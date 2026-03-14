# 环境准备

这份文档用来记录 ROS 2 Jazzy 学习环境怎么进入。

## 你需要知道的两件事

1. ROS 2 安装目录通常在 `/opt/ros/jazzy`
2. 自己工作区编译后，会生成 `install/` 目录

## 常用环境命令

先进入 ROS 2 官方环境：

```bash
source /opt/ros/jazzy/setup.bash
```

如果以后你在当前工作区完成编译，还要再执行：

```bash
source install/setup.bash
```

## 推荐理解方式

- 第一个 `source`：让系统认识 ROS 2
- 第二个 `source`：让系统认识你自己写的包

## 以后可以补充的内容

- Ubuntu 版本
- ROS 2 Jazzy 安装方式
- `colcon` 是否已安装
- `rosdep` 是否已安装

