from tensorflow.keras import optimizers

model.compile(
    optimizer=optimizers.Adam(),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
print("Model compiled successfully")