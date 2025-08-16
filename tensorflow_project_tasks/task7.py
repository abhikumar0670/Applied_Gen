import matplotlib.pyplot as plt

# Dummy history dictionary for demonstration
history = {
    'loss': [1.2, 0.9, 0.7, 0.5, 0.4],
    'val_loss': [1.3, 1.0, 0.8, 0.6, 0.45]
}

plt.plot(history['loss'], label='Training Loss')
plt.plot(history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss (Fine-Tune Model)')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()