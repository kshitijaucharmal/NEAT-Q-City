## Evolving Deep Q-Learning for Sustainable Virtual City Management (INC @ PICT College)

This project investigates the synergy between Deep Q-learning (DQL)
and Neuro-Evolution of Augmenting Topologies (NEAT) for managing a dynamic,
virtual city simulation within the context of the INC competition at PICT College.

The goal is to develop an AI agent that learns optimal decisions to enhance the city's well-being,
balancing factors like air quality, resource management, and economic growth.

**Approach:**

1. **Simulated City Environment:** We create a simulated virtual city environment that captures essential aspects like air quality index, resource levels, and economic indicators. The environment provides state information (e.g., current air quality) and responds to the agent's actions (e.g., building infrastructure).
2. **Deep Q-Learning Agent:** A DQL agent interacts with the simulated city. It receives state information from the environment, employs a deep neural network to predict future rewards for different actions, and takes the action with the highest predicted reward. The agent's performance is evaluated based on a reward function that incentivizes sustainable and beneficial actions for the city.
3. **NEAT for Evolving Network Topologies:** NEAT manages a population of diverse DQL agents with varying network configurations. Through mutation operators (adding/removing connections or nodes) and crossover (combining genetic material), NEAT fosters the evolution of potentially more effective agents across generations. In each generation, agents are evaluated based on their performance within the simulated city, and the best-performing agents are selected for reproduction with variations introduced through mutations.

**Execution:**

1. **Set Up Simulation and Parameters:** Configure the simulation environment, DQL parameters (network architecture, learning rate), and NEAT parameters (population size, mutation rate).
2. **Run NEAT Evolution:** NEAT iterates through generations, evaluating the performance of each agent in the simulated city and selecting the best ones for reproduction with mutations, leading to a population with potentially improved decision-making strategies.
3. **Evaluation and Visualization (Optional):** Track and visualize the performance of agents across generations, analyzing how the evolved agents' actions impact the virtual city's sustainability metrics.

This project explores the potential of combining DQL and NEAT for evolving effective AI agents to manage complex urban environments in a simulated setting. By participating in the INC competition, we aim to showcase this approach and contribute to advancements in AI-powered urban planning and policy optimization.

