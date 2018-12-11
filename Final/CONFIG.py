#ARCHITECTURE PARAMETERS
BEATS_PER_BAR = 96
TOTAL_PIANOROLL_NOTES = 128
LOWEST_NOTE = 23 #Corresponds to C1
NUM_NOTES = 84 #Corresponds to range form C1 to C7
NUM_BARS = 4
NUM_TRACKS = 5
NUM_CLASSES = 3
BATCH_SIZE = 32
NUM_LAYERS = 1

#HYPER PARAMETERS FOR MODEL ARCHITECTURE
LATENT_SIZE = 128
SLOPE_TENSOR = 1.1

#CLASSIFIER TRAINING HYPER PARAMETERS
CLASSIFIER_EPOCHS = 20
CLASSIFIER_LEARNING_RATE = 0.0001
GENRE_LIST = ['alternative', 'rock', 'classic']


#GAN TRAINING HYPER PARAMETERS
GENERATOR_BATCH_SIZE = 16
REAL_DATA_BATCH_SIZE = 16
GENERATOR_LEARNING_RATE = 0.0015
DISCRIMINATOR_LEARNING_RATE = 0.0001
GAN_EPOCHS = 20
NU = 0.825
ZETA = 0.175
BETA_1 = 0.5
BETA_2 = 0.999


#REFINER TRAINING HYPER PARAMETERS
RESIDUAL_LAYERS = 3
LABEL_SMOOTHING = 0
CONFIDENCE_PENTALTY = 0.0
