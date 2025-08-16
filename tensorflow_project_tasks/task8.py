import matplotlib.pyplot as plt

# Dummy history dictionary for demonstration
history = {
    'accuracy': [0.65, 0.75, 0.82, 0.87, 0.9],
    'val_accuracy': [0.62, 0.72, 0.8, 0.85, 0.89]
}

plt.plot(history['accuracy'], label='Training Accuracy')
plt.plot(history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy (Fine-Tune Model)')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()