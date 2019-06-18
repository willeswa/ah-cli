from setuptools import setup

setup(
    name="ah cli",
    version="1.0.0",
    py_module=['firewater'],
    install_requires=[
        'pytest-cov',
        'pytest',
        'requests',
        'flake8',
        'Click'
    ],
    entry_points='''
    [console_scripts]
    firewater=firewater:cli
    ''',
)