import toml
import random
from pprint import pprint


class StatManager:
    def __init__(self, mappings_file="src/stats_manager/data.toml") -> None:
        self.all_stats = {}
        self.all_mappings = {}

        with open(mappings_file) as f:
            # List of mappings
            self.full_data = toml.load(f)
            self.all_mappings = self.full_data["actions"]
            self.all_stats = self.full_data["stats"]

        self.randomize_stats()
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
        # print("Taking action:", action_name)
        for stat in self.all_mappings[action_name].keys():
            self.all_stats[stat] += self.all_mappings[action_name][stat]
        pass
