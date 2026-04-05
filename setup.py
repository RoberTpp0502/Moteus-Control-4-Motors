from setuptools import find_packages, setup

package_name = 'MOTEUS-CONTROL-4-MOTORS'

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
    maintainer='tpp',
    maintainer_email='tpp@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'movem=MOTEUS-CONTROL-4-MOTORS.move_rover:main',
            'movem_by_speed=MOTEUS-CONTROL-4-MOTORS.move_motors_by_a_spec_speed:main',
            'moteus_integ=MOTEUS-CONTROL-4-MOTORS.moteus-integ:main'
        ],
    },
)
