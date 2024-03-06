import json
import random
from pprint import pprint


class StatManager:
    def __init__(self, mappings_file="mappings.json") -> None:
        self.all_stats = {
            "Healthcare": 0.0,
            "Employment": 0.0,
            "Pollution": 0.0,
            "Literacy": 0.0,
            "Recreation": 0.0,
            "GreenSpace": 0.0,
            "PropertyValue": 0.0,
        }
        self.randomize_stats()

        self.all_mappings = {}
        with open(mappings_file) as f:
            # List of mappings
            self.all_mappings = dict(json.load(f))
        pass

    def randomize_stats(self):
        for name, _ in self.all_stats.items():
            self.all_stats[name] = random.random() * 2 - 1

    def print_stats(self):
        print("Current stats: ")
        pprint(self.all_stats)
        print()

    def step(self):
        action = random.choice(list(self.all_mappings.keys()))
        self.take_action(action)
        self.print_stats()

        # inc episode
        pass

    def take_action(self, action_name):
        print("Taking action:", action_name)
        for stat in self.all_mappings[action_name].keys():
            self.all_stats[stat] += self.all_mappings[action_name][stat]
        pass
