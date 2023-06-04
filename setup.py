from setuptools import setup

plugin_identifier = "myplugin"
plugin_package = "Octoprint_Data_Visualiser"
plugin_name = "My Plugin"
plugin_version = "1.0.0"
plugin_description = "A description of my plugin."
plugin_author = "Your Name"
plugin_author_email = "your.email@example.com"
plugin_url = "https://github.com/Loosterlaken/OctoprintPlugin_DataVisualiser.git"
plugin_license = "MIT"

plugin_additional_data = []
plugin_additional_packages = []
plugin_ignored_packages = []
additional_setup_parameters = {}

try:
    import octoprint_setuptools

except:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
	      "the same python installation that OctoPrint is installed under?")
	import sys
	sys.exit(-1)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)
      

setup(
    name=plugin_identifier,
    version=plugin_version,
    packages=[plugin_package],
    url=plugin_url,
    license=plugin_license,
    author=plugin_author,
    author_email=plugin_author_email,
    description=plugin_description,
    install_requires=[
        "octoprint"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: OctoPrint",
        "Environment :: Plugins",
    ],
    entry_points={
        "octoprint.plugin": [
            "myplugin = myplugin"
        ]
    }
)