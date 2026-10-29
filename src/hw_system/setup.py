import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'hw_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Incluir archivos launch
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tu_usuario',
    maintainer_email='tu_email@ejemplo.com',
    description='Sistema de monitorización de hardware',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'emulator_node = hw_system.emulator_node:main',
            'monitor_node = hw_system.monitor_node:main',
            'operator_node = hw_system.operator_node:main',
        ],
    },
)