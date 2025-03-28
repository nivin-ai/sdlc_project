from configparser import ConfigParser

class Config:
    def __init__(self, config_file = "src/sdlc_agenticai/ui/streamlitui/uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE").split(", ")

    def get_llm_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    