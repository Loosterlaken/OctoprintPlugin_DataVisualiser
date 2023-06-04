plugin_package = "Octoprint_Data_Visualiser"
plugin_name = "OctoPrint-Data-Visualiser"
plugin_version = "1.0.0"
plugin_description = """Multiple types of data can be visualised using this plugin"""
plugin_author = "Luuk Oosterlaken"
plugin_author_email = "Luuk.oosterlaken@hotmail.com"
plugin_url = "https://github.com/Loosterlaken/OctoprintPlugin_DataVisualiser.git"
plugin_license = "MIT"
plugin_identifier = "data_visualiser"
plugin_requires = [
	"psutil"
]
plugin_additional_data = []
plugin_additional_packages = []
plugin_ignored_packages = []
additional_setup_parameters = {}

from setuptools import setup

try:
	import octoprint_setuptools
except:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
							"the same python installation that OctoPrint is installed under?")
	import sys

	sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires,
	additional_packages=plugin_additional_packages,
	ignored_packages=plugin_ignored_packages,
	additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
	from octoprint.util import dict_merge

	setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
