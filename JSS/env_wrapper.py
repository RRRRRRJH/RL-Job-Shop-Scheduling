import gym


class MaxStepWrapper(gym.Wrapper):
    def __init__(self, env, max_steps=1000):
        super(MaxStepWrapper, self).__init__(env)
        self.current_step = 0
        self.max_steps = max_steps

    def reset(self, **kwargs):
        observation = super(MaxStepWrapper, self).reset(**kwargs)
        self.current_step = 0
        return observation

    def step(self, action):
        observation, reward, done, info = super(MaxStepWrapper, self).step(action)
        self.current_step += 1
        if self.max_steps <= self.current_step:
            done = True
        return observation, reward, done, info


class BestActionsWrapper(gym.Wrapper):

    def __init__(self, env):
        super(BestActionsWrapper, self).__init__(env)
        self.best_actions = []
        self.current_actions = []
        self.best_score = 0
        self.current_score = 0

    def reset(self, **kwargs):
        observation = super(BestActionsWrapper, self).reset(**kwargs)
        if self.current_score > self.best_score:
            self.best_score = self.current_score
            self.best_actions = self.current_actions
        self.current_score = 0
        self.current_actions = []
        return observation

    def step(self, action):
        observation, reward, done, info = super(BestActionsWrapper, self).step(action)
        self.current_score += reward
        return observation, reward, done, info