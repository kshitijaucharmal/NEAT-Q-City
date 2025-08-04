# 🏙️ Evolving Deep Q-Learning for Sustainable Virtual City Management  
> **INC Competition @ PICT College**



https://github.com/user-attachments/assets/715f0cfa-25ee-43c6-874f-c19d476524db


![City Screenshot 1](https://github.com/user-attachments/assets/774b8fbc-e6a4-4d28-9e7a-2f16df34991a)

---

## 📘 Overview

This project investigates the **synergy between Deep Q-Learning (DQL)** and **Neuro-Evolution of Augmenting Topologies (NEAT)** to manage a **dynamic virtual city simulation**. It was developed for the **INC competition at PICT College**.

Our goal is to evolve intelligent agents capable of **making sustainable decisions** for city growth — optimizing air quality, resource usage, and economic stability.

---

## 🧠 Technologies Used

- **Python 3**
- **Unity (custom environment)**
- **Numpy** – for Deep Q-Network implementation

---

## 🌍 Core Features

✅ **Simulated Urban Environment**  
✅ **Deep Q-Learning Agents**  
✅ **NEAT-based Topology Evolution**  
✅ **Sustainability-Oriented Reward Function**  
✅ **Dynamic Visualization & Logging**

---

## ⚙️ How It Works

### 1. 🏗️ Simulated City Environment

A custom environment captures:
* 🧍‍♂️ **Population Density**
* 🌫️ **Pollution**
* 🏞️ **Recreation**
* 📚 **Literacy Rate**
* 🚓 **Crime Rate**
* 💵 **Household Income**
* 🌳 **Green Space**
* 🏥 **Healthcare**
* 💼 **Employment Rate**
* 🌐 **Internet Coverage**


The environment returns **state vectors** and responds to **agent actions** like upgrading infrastructure, allocating resources, or introducing policies.

---

### 2. 🤖 Deep Q-Learning Agent

Each agent:
- Uses a **neural network** to map states → action-values (Q-values)
- Chooses actions with **ε-greedy** strategy
- Learns via **experience replay** and **Bellman updates**
- Is rewarded for decisions that lead to a more **sustainable and balanced city**

---

### 3. 🧬 NEAT for Evolution

NEAT evolves a **population of DQL agents** by:
- **Mutating network structures** (adding/removing nodes and connections)
- **Crossover** between top-performing agents
- Selecting agents with the **best reward scores** from simulation runs

This enables **dynamic exploration of network topologies** to discover better policies.

---

### 4. 📈 Evaluation & Visualization

Optional logging tools help track:
- Average reward per generation
- Performance trends over time
- Impact of evolved agents on air quality, economy, and resource usage
- Custom Environment in Unity used to visualise and simulate

---

## 📊 Sample Outputs

* 🏥 **Building Hospital**
* 🌳 **Building Park**
* 🏭 **Building Factory**
* 🛣️ **Expand Roads**
* 🏫 **Building Education Institutes**
* 🏘️ **Residential Building**
* 🏢 **Building Offices**
* 🚓 **Building Police Station**
* 📡 **Building Communication Tower**
* 🚜 **Building Farms**

Currently, the simulation can build these buildings, which are placed randomly in the city, but later,
the agent will be able to process a position for the buildings as well

---

## 🏁 Outcome

This hybrid DQL + NEAT approach:
- Adaptively **evolves agent architectures** and **training policies**
- Learns to **balance trade-offs** between air quality, economy, and resource usage
- Demonstrates the potential of **neuro-evolution in urban planning**

---

## 🙌 Acknowledgments

- **INC 2025 @ PICT College** for the platform  
- Research on **NEAT By Kenneth O. Stanley** for guiding our evolution strategy

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---

> _“AI should not just optimize pixels — it should evolve policies that improve life, even in simulations.”_
