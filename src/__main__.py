import numpy as np
from Q_City1.environment import env
from Q_City1.agent import Agent

#should be changed
input_values = [120, 150, 110, 60, 12, 403, 92, 14, 318, 143]

observations_parm = ['Population density', 'Pollution', 'Recreation', 'Literacy rate',
                     'Crime rate', 'Household income', 'Green space', 'Healthcare',
                     'Employment rate', 'Internet coverage']

state = np.array(input_values)
num_states = len(observations_parm)

actions_parm = ['Building hospital', 'Building park', 'Building factory', 'Expand roads',
                'Building education institutes', 'Residential building', 'Building Offices',
                'Building Police station', 'Building Communication tower', 'Building Farms']
num_actions = len(actions_parm)

rewards_Arr = [[0.5, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.4],
               [0.4, -0.4, 0.5, 0.5, 0.4, 0.4, 0.5, 0.4, 0.4, 0.4],
               [-0.5, 0.5, -0.5, -0.4, 0.5, 0.5, -0.4, -0.5, 0.5, 0.5],
               [0.3, -0.3, 0.3, 0.3, -0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
               [0.4, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
               [0.4, -0.3, 0.4, 0.4, -0.3, 0.4, 0.4, 0.4, 0.4, 0.4],
               [0.5, -0.4, 0.5, 0.5, -0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
               [0.5, 0.4, 0.5, 0.5, 0.4, 0.5, 0.4, 0.5, 0.5, 0.5],
               [0.4, 0.4, 0.4, 0.5, 0.4, 0.4, 0.4, 0.5, 0.5, 0.4],
               [0.4, -0.3, 0.4, 0.4, -0.3, 0.4, 0.4, 0.4, 0.4, 0.4]]


def train(agent, num_episodes, env):
    for epoch in range(num_episodes):
        total_reward = 0
        done = False
        state = env.current_state
        #agent.update_target_model()
        print("Epoch:", epoch)
        print(f"-------------------------------------------------------")
        for i in range(10):
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            agent.store_experience(state, action, reward, next_state, done)
            agent.update_q_values()
            state = next_state
            total_reward += reward
            #print("Action:", action, "Reward:", reward, "Total Reward:", total_reward)
            if done:
                break



agent = Agent(num_states=num_states, num_actions=num_actions)
environment = env(state)
train(agent, num_episodes=agent.num_episodes, env=environment)

new_states=np.array([[0,0,1,0,0,0,0,0,0,0]])
pred=agent.predict(new_states)
print(pred)