from Q_City.environment import Environment
from Q_City.agent import Agent
from Q_City.experience_replay import ExperienceReplay
# from Q_City.deepqcolab import Environment
# from Q_City.deepqcolab import Agent

import time


if __name__ == '__main__':


    environment = Environment(no_of_states=10)
    agent = Agent()
    # agent.load(f'models/model_{grid_size}.h5')

    experience_replay = ExperienceReplay(capacity=10000, batch_size=32)
    
    # Number of episodes to run before training stops
    episodes = 5000
    # Max number of steps in each episode
    max_steps = 200

    for episode in range(episodes):

        # Get the initial state of the environment and set done to False
        state = environment.reset()

        # Loop until the episode finishes
        for step in range(max_steps):
            print('Episode:', episode)
            print('Step:', step)
            print('Epsilon:', agent.epsilon)

            # Get the action choice from the agents policy
            action = agent.get_action(state)

            # Take a step in the environment and save the experience
            reward, next_state, done = environment.step(action)
            experience_replay.add_experience(state, action, reward, next_state, done)

            # If the experience replay has enough memory to provide a sample, train the agent
            if experience_replay.can_provide_sample():
                experiences = experience_replay.sample_batch()
                agent.learn(experiences)

            # Set the state to the next_state
            state = next_state
            
            if done:
                break
            
            # Optionally, pause for half a second to evaluate the model
            # time.sleep(0.5)

        #agent.save(f'models/model.h5')