"""
Training loop.
"""

#import glob
#import os
import random
import torch
import libs.statistics


def train(environment, agent, seed=0, n_episodes=10000, max_t=2000,
          gamma=0.99,
          action_repeat=1,
          max_noop=0,
          render=False,
          solve_score=100000.0,
          graph_when_done=False):
    """
    Params
    ======
        environment: environment object
        agent: agent object
        seed (int): Random seed
        n_episodes (int): maximum number of training episodes
        max_t (int): maximum number of timesteps per episode
        gamma (float): discount rate
        action_repeat (int): number of times to repeat same action
        max_noop (int): maximum number of initial noops at start of episode
        render (bool): whether to render the agent
        solve_score (float): criteria for considering the environment solved
        graph_when_done (bool): whether to show matplotlib graphs of the training run
    """
    random.seed(seed)
    stats = libs.statistics.Stats()
    stats_format = ''

    # remove checkpoints from prior run
    #prior_checkpoints = glob.glob('checkpoints/last_run/episode*.pth')
    #for checkpoint in prior_checkpoints:
    #    os.remove(checkpoint)

    for i_episode in range(1, n_episodes+1):
        saved_log_probs = []
        rewards = []
        state = environment.reset()
        # take a random amount of noop actions before starting episode to inject stochasticity
        for i in range(random.randint(0, max_noop)):
            if render:  # optionally render agent
                environment.render()
            state, reward, done = environment.step(0)
        # training loop
        for t in range(1, max_t+1):
            if render:  # optionally render agent
                environment.render()
            if t % action_repeat == 1 or action_repeat == 1:
                action, log_prob = agent.act(state)
            saved_log_probs.append(log_prob)
            state, reward, done = environment.step(action)
            rewards.append(reward)
            if done:
                break

        # every episode
        if environment.name == 'ppaquette/meta-SuperMarioBros-Tiles-v0':
            rewards[0] = 0  # for some reason SuperMarioBros env gives huge reward on first step, distorting the reward function
        agent.learn(rewards, saved_log_probs, gamma)
        stats.update(t, rewards, i_episode)
        stats.print_episode(i_episode, t, stats_format)

        # every epoch (100 episodes)
        if i_episode % 100 == 0:
            stats.print_epoch(i_episode, stats_format)
            save_name = 'checkpoints/last_run/episode.{}.pth'.format(i_episode)
            torch.save(agent.model.state_dict(), save_name)

        # if solved
        if stats.is_solved(i_episode, solve_score):
            stats.print_solve(i_episode, stats_format)
            torch.save(agent.model.state_dict(), 'checkpoints/last_run/solved.pth')
            break

    # training finished
    if graph_when_done:
        stats.plot()
