import numpy as np
from simple_rl.agents import QLearningAgent, SARSAAgent
from simple_rl.tasks import GridWorldMDP
from simple_rl.run_experiments import run_agents_on_mdp

# Setup MDP.
mdp = GridWorldMDP(width=4, height=3, init_loc=(1, 1), goal_locs=[(4, 3)], lava_locs=[(4, 2)], gamma=0.95, walls=[(2, 2)], slip_prob=0.1)

# Setup Agents.
ql_agent = QLearningAgent(actions=mdp.get_actions())

sarsa_agent = SARSAAgent(
    actions=env_cliff_walking.get_actions(),
    alpha=0.1,
    gamma=0.9,
    epsilon=0.1,
    name="SARSA"
)


# Run experiment and make plot.
run_agents_on_mdp([ql_agent], mdp, instances=5, episodes=50, steps=10)
