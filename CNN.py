import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# 1️⃣ Dataset paths (Change these paths as needed)
train_dir = r'C:\Users\HP\Downloads\cats_and_dogs_filtered\cats_and_dogs_filtered\train'
test_dir = r'C:\Users\HP\Downloads\cats_and_dogs_filtered\cats_and_dogs_filtered\validation'

# 2️⃣ Image data generator (Normalization)
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# 3️⃣ Load dataset from folders
train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),   # resize all images
    batch_size=32,
    class_mode='binary'       # cats vs dogs → binary classification
)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# 4️⃣ Build CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')   # binary → sigmoid
])

# 5️⃣ Compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 6️⃣ Train model
history = model.fit(
    train_data,
    epochs=5,
    validation_data=test_data
)

# 7️⃣ Evaluate model
test_loss, test_acc = model.evaluate(test_data, verbose=2)
print(f"✅ Test Accuracy: {test_acc:.4f}")

# 8️⃣ Plot accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('CNN Cats vs Dogs')
plt.show()
