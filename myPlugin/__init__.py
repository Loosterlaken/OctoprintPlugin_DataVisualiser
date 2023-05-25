# Octoprint DIY plugin builder library
import octoprint.plugin

class DataVisualiser( octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin):
    def get_template_configs(self):
        return [
            dict(type="tab", name="Graph", template="Github_example1.jinja2", custom_bindings=True)
        ]
    
    def on_after_startup(self):
        # data  opslag locatie
        #log = open("d:\Log.txt","a")
        while True:
            self._logger.info("Hij doet nu iets")

    
    
    #def on_event(Startup): #Event should become "PrintStarted"
    #    while True:

__plugin_name__ = "Particulate matter measurement"
__plugin_version__ = "1.0.0"
__plugin_description__ = "SDS011 sensor setup and visualisation in tab"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = DataVisualiser()