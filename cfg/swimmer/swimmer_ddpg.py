algorithm='ddpg'
env_class='Gym'
model_class='LowDim2x'

environment = {
    'name': 'Swimmer-v2',
}

model = {
    'state_size': 8,
    'action_size': 2,
    'fc1_units': 400,
    'fc2_units': 300
}

agent = {
    'action_size': 2,
    #'buffer_size': int(3e5),
    'batch_size': 128,
    #'weight_decay': 0.0,
    #'evaluation_only': True
}

train = {
    'n_episodes': 100000,
    'max_t': 200,
    #'solve_score': 2000.0,
}