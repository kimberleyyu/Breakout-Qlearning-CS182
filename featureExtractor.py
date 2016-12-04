# feature extractor script
# CS182 Project
# Kimberley Yu
# 12-04-2016

# take openAI gym breakout environment and generate features for approximate Q-learning

import gym
env = gym.make('Breakout-v0')
env.reset()
for _ in range(1000):
    env.render()
    #env.step(env.action_space.sample()) # take a random action
