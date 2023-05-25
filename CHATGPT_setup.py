from setuptools import setup

setup(
    name="data_visualiser",
    version="1.0.0",
    author="Your Name",
    description="Multiple types of data can be visualised using this plugin",
    packages=["data_visualiser"],
    entry_points={
        "octoprint.plugin": [
            "data_visualiser = data_visualiser:DataVisualiser"
        ]
    },
    python_requires=">=3.7,<4",
)