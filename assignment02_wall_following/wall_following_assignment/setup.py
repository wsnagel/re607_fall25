from setuptools import find_packages, setup

package_name = 'wall_following_assignment'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ground_truth_tf_publisher = wall_following_assignment.ground_truth_tf_publisher:main',
            'wall_follower = wall_following_assignment.wall_follower:main',
        ],
    },
)


