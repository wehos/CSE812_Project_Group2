CONFIGS_ = {
    # input_channel, n_class, hidden_dim, latent_dim
    'cifar': ([16, 'M', 32, 'M', 'F'], 3, 10, 2048, 64),
    'cifar100-c25': ([32, 'M', 64, 'M', 128, 'F'], 3, 25, 128, 128),
    'cifar100-c30': ([32, 'M', 64, 'M', 128, 'F'], 3, 30, 2048, 128),
    'cifar100-c50': ([32, 'M', 64, 'M', 128, 'F'], 3, 50, 2048, 128),
    'emnist': ([6, 16, 'F'], 1, 25, 784, 32),
    'mnist': ([6, 16, 'F'], 1, 10, 784, 32),
    
    # 'mnist_0': ([6, 16, 'F'], 1, 10, 784, 32),
    # 'mnist_1': ([6, 18, 'F'], 1, 10, 882, 32),
    # 'mnist_2': ([6, 20, 'F'], 1, 10, 980, 32),
    # 'mnist_3': ([6, 22, 'F'], 1, 10, 1078, 32),
    # 'mnist_4': ([6, 24, 'F'], 1, 10, 1176, 32),
    # 'mnist_5': ([6, 26, 'F'], 1, 10, 1274, 32),
    # 'mnist_6': ([6, 28, 'F'], 1, 10, 1372, 32),
    # 'mnist_7': ([6, 30, 'F'], 1, 10, 1470, 32),
    # 'mnist_8': ([6, 32, 'F'], 1, 10, 1568, 32),
    # 'mnist_9': ([6, 34, 'F'], 1, 10, 1666, 32),
    # 'mnist_10': ([6, 36, 'F'], 1, 10, 1764, 32),
    # 'mnist_11': ([6, 38, 'F'], 1, 10, 1862, 32),
    # 'mnist_12': ([6, 40, 'F'], 1, 10, 1960, 32),
    # 'mnist_13': ([6, 42, 'F'], 1, 10, 2058, 32),
    # 'mnist_14': ([6, 44, 'F'], 1, 10, 2156, 32),
    # 'mnist_15': ([6, 46, 'F'], 1, 10, 2254, 32),
    # 'mnist_16': ([6, 48, 'F'], 1, 10, 2352, 32),
    # 'mnist_17': ([6, 50, 'F'], 1, 10, 2450, 32),
    # 'mnist_18': ([6, 52, 'F'], 1, 10, 2548, 32),
    # 'mnist_19': ([6, 54, 'F'], 1, 10, 2646, 32),



    # 'mnist_0': ([4, 18, 'F'], 1, 10, 882, 32),
    # 'mnist_1': ([4, 10, 18, 'F'], 1, 10, 288, 32),
    'mnist_0': ([4, 10, 18, 28, 'F'], 1, 10, 112, 32),

    
    'mnist_cnn1': ([6, 'M', 16, 'M', 'F'], 1, 10, 64, 32),
    'mnist_cnn2': ([16, 'M', 32, 'M', 'F'], 1, 10, 128, 32),
    'celeb': ([16, 'M', 32, 'M', 64, 'M', 'F'], 3, 2, 64, 32)
}

# temporary roundabout to evaluate sensitivity of the generator
GENERATORCONFIGS = {
    # hidden_dimension, latent_dimension, input_channel, n_class, noise_dim
    'cifar': (512, 32, 3, 10, 64),
    'celeb': (128, 32, 3, 2, 32),
    'mnist': (256, 32, 1, 10, 32),
    'mnist-cnn0': (256, 32, 1, 10, 64),
    'mnist-cnn1': (128, 32, 1, 10, 32),
    'mnist-cnn2': (64, 32, 1, 10, 32),
    'mnist-cnn3': (64, 32, 1, 10, 16),
    'emnist': (256, 32, 1, 25, 32),
    'emnist-cnn0': (256, 32, 1, 25, 64),
    'emnist-cnn1': (128, 32, 1, 25, 32),
    'emnist-cnn2': (128, 32, 1, 25, 16),
    'emnist-cnn3': (64, 32, 1, 25, 32),
}

RUNCONFIGS = {
    'emnist':
        {
            'ensemble_lr': 1e-4,
            'ensemble_batch_size': 128,
            'ensemble_epochs': 50,
            'num_pretrain_iters': 20,
            'ensemble_alpha': 1,  # teacher loss (server side)
            'ensemble_beta': 0,  # adversarial student loss
            'unique_labels': 25,
            'generative_alpha': 10,
            'generative_beta': 1,
            'weight_decay': 1e-2
        },

    'mnist':
        {
            'ensemble_lr': 3e-4,
            'ensemble_batch_size': 128,
            'ensemble_epochs': 50,
            'num_pretrain_iters': 20,
            'ensemble_alpha': 1,  # teacher loss (server side)
            'ensemble_beta': 0,  # adversarial student loss
            'ensemble_eta': 1,  # diversity loss
            'unique_labels': 10,  # available labels
            'generative_alpha': 10,  # used to regulate user training
            'generative_beta': 10,  # used to regulate user training
            'weight_decay': 1e-2
        },

    'celeb':
        {
            'ensemble_lr': 3e-4,
            'ensemble_batch_size': 128,
            'ensemble_epochs': 50,
            'num_pretrain_iters': 20,
            'ensemble_alpha': 1,  # teacher loss (server side)
            'ensemble_beta': 0,  # adversarial student loss
            'unique_labels': 2,
            'generative_alpha': 10,
            'generative_beta': 10,
            'weight_decay': 1e-2
        },

}
