# 常用命令

下面这些命令是学习 ROS 2 最常见的一批。

## 环境相关

```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
```

## 构建相关

```bash
colcon build
```

作用：编译当前工作区里的 ROS 2 package。

## 运行相关

```bash
ros2 run <包名> <可执行文件名>
ros2 launch <包名> <launch文件名>
```

## 查看信息

```bash
ros2 pkg list
ros2 node list
ros2 topic list
ros2 service list
```

## 当前阶段先记住

- `colcon build`
- `ros2 run`
- `ros2 topic list`

这三个命令先熟悉，后面会经常用到。

