# Imports
from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

# Run Experiment
mdp = GridWorldMDP(goal_locs=[(5, 3)])
agent = QLearningAgent(mdp.get_actions())
run_agents_on_mdp([agent], mdp)
