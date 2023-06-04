# Octoprint DIY plugin builder library
import octoprint.plugin

class DataVisualiser( octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin):
    def get_template_configs(self):
        return [
            dict(type="tab", name="Graph", template="Github_example2.jinja2", custom_bindings=True)
        ]
    
    def on_after_startup(self):
        # Voeg hier je eigen logica toe voor het verzamelen en verwerken van gegevens
        
        # Laad de sjabloon en render deze met de gegevens
        rendered_template = self._plugin_manager.get_template("Github_example2.jinja2").render(
            # Voeg hier je eigen gegevens toe om door te geven aan de sjabloon
        )

    
    
    #def on_event(Startup): #Event should become "PrintStarted"
    #    while True:

__plugin_name__ = "Data visualiser"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Multiple types of data can be visualised using this plugin"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = DataVisualiser()