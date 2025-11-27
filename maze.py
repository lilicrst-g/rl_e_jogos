#!/usr/bin/env python

# Python imports.
from __future__ import print_function
import argparse

# Other imports.
#import srl_example_setup
from simple_rl.agents import QLearningAgent
from simple_rl.run_experiments import run_single_agent_on_mdp 
from simple_rl.tasks import GridWorldMDP
from simple_rl.tasks.grid_world.GridWorldMDPClass import make_grid_world_from_file
from simple_rl.planning import ValueIteration

def parse_args():
    # Add all arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", type=str, default="learning", nargs='?', help="Choose the visualization type (one of {value, policy, agent, learning or interactive}).")
    args = parser.parse_args()
    return args.v

def main():
    
    # Setup MDP, Agents.
    mdp = GridWorldMDP(
        width=9, 
        height=9, 
        init_loc=(1, 1), 
        goal_locs=[(9, 1)],  
        lava_locs=[(1, 9), (6, 3), (9, 7)], 
        gamma=0.95, 
        walls=[
                (2, 2), (2, 3), (2, 4), (2, 7), (2, 8), (2, 9), 
                (3, 7),
                (4, 2), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), 
                (5, 2),
                (6, 2), (6, 8),
                (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), 
                (8, 1), (8, 5), (8, 8), 
                (9, 3), (9, 8)
        ], 
        slip_prob=0.1
        )
    ql_agent = QLearningAgent(mdp.get_actions(), epsilon=0.2, alpha=0.2)
    viz = parse_args()

    # Choose viz type.
    viz = "learning"

    if viz == "value":
        # --> Color corresponds to higher value.
        # Run experiment and make plot.
        mdp.visualize_value()
    elif viz == "policy":
        # Viz policy
        value_iter = ValueIteration(mdp)
        value_iter.run_vi()
        policy = value_iter.policy
        mdp.visualize_policy(policy)
    elif viz == "agent":
        # --> Press <spacebar> to advance the agent.
        # First let the agent solve the problem and then visualize the agent's resulting policy.
        print("\n", str(ql_agent), "interacting with", str(mdp))
        run_single_agent_on_mdp(ql_agent, mdp, episodes=500, steps=200)
        mdp.visualize_agent(ql_agent)
    elif viz == "learning":
        # --> Press <r> to reset.
        # Show agent's interaction with the environment.
        mdp.visualize_learning(ql_agent, delay=0.005)
    elif viz == "interactive":
        # Press <1> up, <2> down, <3> left, <4> right.
    	mdp.visualize_interaction()


if __name__ == "__main__":
    main()