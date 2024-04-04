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
            self.all_stats[name] = random.random()

    def print_stats(self):
        print("Current stats: ")
        pprint(self.all_stats)
        print()

    def take_random_action(self):
        action = random.choice(list(self.all_mappings.keys()))
        self.take_action(action)
        pass

    def take_action(self, action_name):
        for stat in self.all_mappings[action_name].keys():
            change = self.all_mappings[action_name][stat]
            self.all_stats[stat] += change * 0.1
            self.all_stats[stat] = self.clamp(self.all_stats[stat], 0.0000, 1.0000)
        pass

    def sample(self):
        actions = list(self.all_mappings.keys())
        n = random.randint(0, len(actions) - 1)
        return (actions[n], n)

    def clamp(self, stat, min, max):
        if stat < min:
            return min
        elif stat > max:
            return max
        else:
            return stat
