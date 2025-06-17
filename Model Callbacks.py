from tensorflow.keras.callbacks import EarlyStopping

def my_early_callback():
    return EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    )