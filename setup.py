from setuptools import setup
setup(
    install_requires=[
        "meerk40t>=0.7.0-post40",
    ],
    extras_require={
        'cv': ["opencv-python-headless>=3.4.0.0"],
        'cvhead': ["opencv-python>=3.4.0.0"],
    }
)