from setuptools import setup
import os


HERE = os.path.abspath(os.path.dirname(__file__))

with open('README.rst', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="youtube-notifier",
    version="0.1",
    url="https://github.com/thequietestoctopus/youtube-notifier",
    license="MIT",
    author="quietoctopus",
    install_requires=[
        "beautifulsoup4~=4.9.1",
        "requests~=2.24.0",
    ],
    author_email="cullenoboyle@gmail.com",
    description="Automated messages for specified youtube channels via Telegram",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    entry_points={
        "console_scripts": [
            "youtube_notifier = youtube_notifier.__main__:main",
        ],
    },
    packages=["youtube_notifier"],
    include_package_data=True,
    platforms="any",
    package_data={"youtube_notifier": ["data/*.json"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)