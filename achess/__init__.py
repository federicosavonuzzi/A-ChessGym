from gymnasium.envs.registration import register

register(
    id='AchessEnv',
    entry_point='achess.envs:AchessEnv',
)

