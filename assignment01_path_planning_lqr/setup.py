import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'assignment01_path_planning_lqr'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('lib/' + package_name, [package_name + '/lqr.py', package_name + '/plotting_utils.py', package_name + '/priority_queue.py']),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.pkl')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wsnagel',
    maintainer_email='wsnagel@widener.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'astar = assignment01_path_planning_lqr.astar_planner:main',
             'dijkstra = assignment01_path_planning_lqr.dijkstra_planner:main',
             'rrt = assignment01_path_planning_lqr.rrt_planner:main',
             'lqr_tracking_example = assignment01_path_planning_lqr.linear_model_trajectory_following:main',
             'lqr_example = assignment01_path_planning_lqr.omni_car_with_friction:main',
             'lqr_hw = assignment01_path_planning_lqr.lqr_hw:main',
        ],
    },
)
