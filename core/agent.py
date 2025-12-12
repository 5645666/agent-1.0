from core.classifier import classify_message
from core.generator import generate_response
from core.scenario_loader import ScenarioLoader

class Agent:
    def __init__(self):
        self.scenarios = ScenarioLoader()

    def handle_message(self, message: str) -> str:
        message_type = classify_message(message)
        scenario = self.scenarios.get(message_type)

        return generate_response(message, scenario)
