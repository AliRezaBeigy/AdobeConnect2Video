import setuptools
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AdobeConnect2Video",
    version="1.1.1",
    license="MIT",
    author="AliReza Beigy",
    author_email="AliRezaBeigyKhu@gmail.com",
    entry_points={
        "console_scripts": [
            "AdobeConnect2Video=AdobeConnect2Video.__main__:main",
        ]
    },
    include_package_data=True,
    package_data={
        'AdobeConnect2Video': ["no_video.jpg"]
    },
    python_requires=">=3.6",
    install_requires=[
        'untangle',
    ],
    platforms=["nt", "posix"],
    long_description=long_description,
    packages=setuptools.find_packages(),
    url="https://github.com/AliRezaBeigy/AdobeConnect2Video",
    long_description_content_type="text/markdown",
    description="A handy tool to convert adobe connect zip data into a single video file",
    keywords="adobe-connect ffmpeg",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)
