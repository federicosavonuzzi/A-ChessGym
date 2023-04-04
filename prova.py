import gymnasium as gym 
import achess

env=gym.make("AchessEnv", render_mode="human")
observation, info = env.reset()

for _ in range(1000):
	action = env.action_space.sample()
	reward, terminated = env.step(action)
	
	if terminated or truncated:
		observation, info = env.reset()

env.close()
