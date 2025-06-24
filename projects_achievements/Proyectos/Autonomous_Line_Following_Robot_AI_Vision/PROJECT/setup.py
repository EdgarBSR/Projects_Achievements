from setuptools import find_packages, setup
import os 
from glob import glob
package_name = 'PROJECT'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kokas',
    maintainer_email='kokas@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_node = PROJECT.test_node:main',
            'color_detector = PROJECT.color_detector:main',
            'photo = PROJECT.image:main',
            'controller = PROJECT.controller:main',
            'odometry = PROJECT.odometry:main',
            'publish = PROJECT.publish:main',
            'move = PROJECT.move:main',
            'AI = PROJECT.AI_light:main',
            'AI2 = PROJECT.AI_signal:main',
            'show = PROJECT.show:main',
            'crossing = PROJECT.crossing:main',
            'odometry2 = PROJECT.odometry2:main',
            'controller2 = PROJECT.controller2:main',
            'tracker = PROJECT.color_tracker:main',
            'line_follower = PROJECT.line_follower:main',
            'line_follower_final = PROJECT.line_follower_final:main',
            'line_follower_best = PROJECT.line_follower_best:main',
            'fuzzy = PROJECT.fuzzy:main',
            'square = PROJECT.square:main',
            'odometry_cross = PROJECT.odometry_cross:main',
            'points_cross = PROJECT.points_cross:main'
        ],
    },
)
