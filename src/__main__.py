import numpy as np
from Q_City.environment import env
from Q_City.agent import Agent
from neat.geneh import GeneHistory

# should be changed
num_states = 10
num_actions = 10

rewards_Arr = [
    [0.5, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.4],
    [0.4, -0.4, 0.5, 0.5, 0.4, 0.4, 0.5, 0.4, 0.4, 0.4],
    [-0.5, 0.5, -0.5, -0.4, 0.5, 0.5, -0.4, -0.5, 0.5, 0.5],
    [0.3, -0.3, 0.3, 0.3, -0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    [0.4, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
    [0.4, -0.3, 0.4, 0.4, -0.3, 0.4, 0.4, 0.4, 0.4, 0.4],
    [0.5, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
    [0.5, 0.4, 0.5, 0.5, 0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
    [0.4, 0.4, 0.4, 0.5, 0.4, 0.4, 0.4, 0.5, 0.5, 0.4],
    [0.4, -0.3, 0.4, 0.4, -0.3, 0.4, 0.4, 0.4, 0.4, 0.4],
]


gh = GeneHistory(num_states, num_actions)
agent = Agent(num_states=num_states, num_actions=num_actions, gene_history=gh)
environment = env(state)
train(agent, num_episodes=agent.num_episodes, env=environment)

new_states = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])
pred = agent.predict(new_states)
print(pred)
