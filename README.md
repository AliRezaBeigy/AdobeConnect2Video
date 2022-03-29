# AdobeConnect2Video

![PyPI](https://img.shields.io/pypi/v/AdobeConnect2Video?style=for-the-badge)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://github.com/AliRezaBeigy/AdobeConnect2Video/blob/master/LICENSE)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
![GitHub Repo stars](https://img.shields.io/github/stars/AliRezaBeigy/AdobeConnect2Video?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/AdobeConnect2Video?style=for-the-badge)

A handy tool to convert adobe connect zip data into a single video file

## Requirement

- Python 3
- FFMPEG
  - Download [ffmpeg](https://www.ffmpeg.org/download.html) and put the installation path into PATH enviroment variable 

## Quick Start

You need to [ffmpeg](https://www.ffmpeg.org) to use this app, so you can simply download ffmpeg from [Official Site](https://www.ffmpeg.org/download.html) then put the installation path into PATH enviroment variable

Now you should install AdobeConnect2Video as global app:

```shell
$ pip install -U AdobeConnect2Video
or
$ python -m pip install -U AdobeConnect2Video
```

**Use `-U` option to update AdobeConnect2Video to the last version**

## Usage

Download the adobe connect zip data by adding following path to the address of online recorded class
```url
output/ClassName.zip?download=zip
```
for exmple if you online recorded class link is
```url
http://online.GGGGG.com/p81var0hcdk5/
```
you can download zip data from following link
```url
http://online.GGGGG.com/p81var0hcdk5/output/ClassName.zip?download=zip
```
Then extract the zip in 'data' directory and install AdobeConnect2Video from pip
```shell
$ AdobeConnect2Video

$ AdobeConnect2Video -i [classId]
```

Example:
If data extracted into 'Course1' directory inside 'data' directory and you want to have output in 'output' directory with 480x470 resolution you can use following command 
```shell
$ AdobeConnect2Video -i Course1 -d data -o output -r 480x470
```

For more details:

```text
$ AdobeConnect2Video -h
usage: AdobeConnect2Video [-h] -i ID [-d DATA_PATH] [-o OUTPUT_PATH] [-r RESOLUTION]

options:
  -h   --help          show this help message and exit
  -i   --id            the name of directory data is available
  -d   --data-path     the path extracted data must be available as directory
  -o   --output-path   the output path that generated data saved
  -r   --resolution    the resolution of output video
```

## Contributions

If you're interested in contributing to this project, first of all I would like to extend my heartfelt gratitude.

Please feel free to reach out to me if you need help. My Email: AliRezaBeigyKhu@gmail.com
Telegram: [@AliRezaBeigy](https://t.me/AliRezaBeigyKhu)

## LICENSE

MIT
