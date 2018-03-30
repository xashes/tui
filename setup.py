from setuptools import setup

package = 'tui'
version = '0.1'

setup(
    name=package,
    version=version,
    description="The front end of my trade data analysis.",
    url='https://github.com/xashes/tui',
    packages=['tui'],
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
