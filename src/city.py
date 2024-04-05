from stats_manager.manager import StatManager
from Q_City.agent import Agent
from Q_City.environment import env


class City:
    def __init__(self, gh) -> None:
        # assigning a manager to the city
        self.manager = StatManager()
        self.gh = gh
        # assigning an agent to the city
        self.agent = Agent(
            num_states=len(self.manager.all_stats),
            num_actions=len(self.manager.all_mappings),
            gene_history=self.gh,
        )
        # The brain given by neat
        self.agent.init_model()

        self.stats = list(self.manager.all_stats.values())
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
        self.env = env(self.stats_list())

        self.done = False
        self.batch_size = 32
        self.ctr = 0
        pass

    def clone(self):
        c = City(self.gh)
        c.stats = self.stats
        c.manager.all_stats = self.manager.all_stats
        c.agent.reset_model(self.agent.g)
        return c

    def city_details(self, action_taken):
        msg = ",".join(str(round(v, 4)) for v in self.stats)
        msg += "," + str(action_taken)
        return msg

    def take_action(self):
        action = self.agent.select_action(self.stats_list())
        # updating stats_manager
        # self.manager.take_action(action)
        # self.stats = list(self.manager.all_stats.values())
        return action

    def stats_list(self):
        return [round(s, 4) for s in self.stats]

    def mutate(self):
        self.agent.g.mutate()
        pass

    def calculate_fitness(self):
        for stat, score in self.manager.all_stats.items():
            self.fitness += self.weights[stat] * score

    def train(self):
        total_reward = 0
        state = self.env.current_state
        self.ctr += 1
        if self.batch_size % self.ctr == 0:
            self.agent.update_target_model()

        action = self.take_action()
        next_state, reward, self.done = self.env.step(action)
        self.agent.store_experience(state, action, reward, next_state, self.done)
        self.agent.update_q_values()
        state = next_state
        self.stats = state
        total_reward += reward
        # print("Action:", action, "Reward:", reward, "Total Reward:", total_reward)
        if self.done:
            return -1
        return action
