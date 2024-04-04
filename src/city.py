from stats_manager.manager import StatManager
from Q_City.agent import Agent


class City:
    def __init__(self) -> None:
        # assigning a manager to the city 
        self.manager = StatManager()
        # assigning an agent to the city
        self.agent=Agent(num_states=len(self.manager.all_stats),num_actions=len(self.manager.all_mappings))
        # The brain given by neat
        self.brain = Agent.init_model()

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
        pass

    def city_details(self, action_taken):
        msg = ",".join(str(round(v, 4)) for v in self.stats.values())
        msg += "," + str(action_taken)
        return msg

    def take_action(self):
        action=Agent.select_action(self.stats_list())
        # if not action:
        #     action, _ = self.manager.sample()
        print(f"Action:",action)
        #updating stats_manager
        self.manager.take_action(action)
        self.stats = self.manager.all_stats
        return action

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


# main function()
            X=City()
            print(X.stats)
