import json
import os

class ScenarioLoader:
    def __init__(self, folder="scenarios"):
        self.folder = folder

    def get(self, scenario_name: str):
        path = os.path.join(self.folder, f"{scenario_name}.json")

        if not os.path.exists(path):
            return {"default": "Извините, я пока не знаю, как ответить 🤍"}

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
