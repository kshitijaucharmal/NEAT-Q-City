from stats_manager.manager import StatManager


class City:
    def __init__(self) -> None:
        self.manager = StatManager()
        self.stats = self.manager.all_stats
        self.weights = {
            "Population": 0.1,
            "Pollution": -0.3,
            "Recreation": 0.2,
            "Employment": 0.25,
            "Literacy": 0.15,
            "Crime": 0.25,
            "HouseholdIncome": 0.3,
            "GreenSpace": 0.1,
            "Healthcare": 0.2,
            "InternetCoverage": 0.15,
        }
        self.fitness = 0

        # The brain given by neat
        self.brain = None
        pass

    def reset(self):
        self.manager = StatManager()
        self.stats = self.manager.all_stats
        self.fitness = 0

        # self.brain.reset()
        pass

    def city_details(self, action_taken):
        msg = ",".join(str(round(v, 4)) for v in self.stats.values())
        msg += "," + str(action_taken)
        return msg

    def take_action(self, action=None):
        if not action:
            action, _ = self.manager.sample()
        self.manager.take_action(action)
        self.stats = self.manager.all_stats
        # print(list(self.stats.values()))
        pass

    def stats_list(self):
        return [round(s, 4) for s in list(self.stats.values())]

    def crossover(self, partner):
        # child = self.brain.crossover(partner.brain)
        child = partner

        return child

    def mutate(self):
        # self.brain.mutate()
        pass

    def calculate_fitness(self):
        for stat, score in self.stats.items():
            self.fitness += self.weights[stat] * score
