# ROS 2 Jazzy 学习项目

这是一个面向零基础学习者的 ROS 2 Jazzy 练习仓库。

当前目标不是一开始就做复杂项目，而是先把学习环境、常用命令、笔记结构整理好，再逐步创建 ROS 2 package 并练习节点通信。

目前仓库也开始从 ROS 2 基础学习，逐步过渡到“项目化原型练习”的阶段，但仍然以便于理解和动手验证为主。

## 目录说明

- `docs/`：放环境配置和常用命令说明
- `notes/`：放每天的学习笔记
- `src/`：以后存放 ROS 2 package

## 建议学习顺序

1. 理解 workspace、package、node 的基本概念
2. 学会进入 ROS 2 环境
3. 认识常用命令
4. 再开始创建第一个 Python package

## 当前阶段

目前这个仓库已经有基础学习包，也开始加入简单的项目原型演示包。

后续会逐步补充：

- 第一个 Python 节点
- 发布者与订阅者
- service 和 client
- launch 和 parameter

## 当前 package

- `py_basics`：用于基础的 publisher、subscriber、topic、parameter 学习
- `sensor_pipeline_demo`：用于模拟项目中的多传感器输入与 `/odom_status` 输出链路

## 运行示例

先进入 ROS 2 Jazzy 环境并编译工作区：

```bash
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

运行 `sensor_pipeline_demo` 中的演示节点：

```bash
ros2 run sensor_pipeline_demo fake_odometry_node
```

当前这个节点会：

- 订阅 `/lidar_points`
- 订阅 `/imu_data`
- 发布 `/odom_status`

当它同时收到 lidar 和 imu 消息后，会发布一条字符串状态消息，用来演示最简单的数据链路。
