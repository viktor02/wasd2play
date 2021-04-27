from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wasd2play',
    version='0.4.6',
    packages=['wasd2play'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests>=2.24.0"],
    url='https://github.com/viktor02/wasd2play',
    license='MIT',
    author='Viktor Karpov',
    author_email='v@vitka-k.ru',
    description='Open wasd.tv streams in your favorite player!',
    entry_points={
        'console_scripts': [
            'wasd2play=wasd2play:main',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
