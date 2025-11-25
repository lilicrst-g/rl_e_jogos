## 🚀 Teste rápido com Q-Learning

# run_zombie.py
from simple_rl.agents import QLearningAgent
from simple_rl.run_experiments import run_agents_on_mdp
from zombie_chase_mdp import ZombieChaseMDP

mdp = ZombieChaseMDP(width=6, height=6, goal=(6,6))
agent = QLearningAgent(actions=mdp.get_actions(), alpha=0.1, epsilon=0.2, gamma=0.99)

run_agents_on_mdp(
    agents=[agent],
    mdp=mdp,
    instances=5,
    episodes=200,
    steps=60,
    verbose=True
)

