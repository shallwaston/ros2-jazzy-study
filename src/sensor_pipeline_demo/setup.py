from setuptools import find_packages, setup

package_name = 'sensor_pipeline_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shallwaston',
    maintainer_email='shallwaston@todo.todo',
    description='Simple sensor pipeline demo for ROS 2 Jazzy learning.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fake_odometry_node = sensor_pipeline_demo.fake_odometry_node:main',
        ],
    },
)
