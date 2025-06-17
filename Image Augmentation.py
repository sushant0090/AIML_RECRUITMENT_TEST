from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_aug_pipeline():
    aug = ImageDataGenerator(
        rotation_range=20,
        horizontal_flip=True,
        zoom_range=0.2
    )
    return aug
