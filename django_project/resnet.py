import tensorflow as tf
import keras
# from keras.preprocessing.image import ImageDataGenerator
# from keras.layers import Dense, GlobalAveragePooling2D
from keras._tf_keras.keras.optimizers import Adam
from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras.models import load_model
import natsort
import os
import numpy as np
import cv2

batch_size = 32
image_rows = 224
image_cols = 224

# 경로에 한글있으면 안됨
img_path = 'C:/find_poster/train/posters/'

image_fns = natsort.natsorted(os.listdir(img_path))
image_fns = np.array(image_fns)
size = len(image_fns)
print(image_fns)
train_data = np.zeros((size, image_rows, image_cols, 3), dtype=np.uint8)
train_label = np.zeros((size, 19), dtype=np.uint8)

for i in range(size):
        img = cv2.imread(os.path.join(img_path, image_fns[i]), cv2.IMREAD_COLOR)
        tmp = cv2.resize(img, (image_cols, image_rows), interpolation=cv2.INTER_CUBIC)

        train_data[i,:,:,:] = tmp
        
        filename = list(image_fns[i].split('_')[1].split('.')[0])
        filename = list(map(int, filename))
        filename = np.array(filename)
        train_label[i, :] = filename
        
train_data = np.array(train_data).astype(np.float32)/255
print(train_data.shape, train_label.shape)

# Load pre-trained ResNet50 model without top layers
base_model = keras.applications.ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze base model layers
for layer in base_model.layers[:45]:
    layer.trainable = False

# Add new classification layers
x = base_model.output
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dense(1024, activation='relu')(x)
predictions = keras.layers.Dense(19, activation='softmax')(x)  # Adjust 'num_classes' according to your dataset

# Create new model
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer=Adam(learning_rate = 0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
# model.summary()

# Train the model with your dataset
# train_datagen = ImageDataGenerator(rescale=1./255)
# train_generator = train_datagen.flow_from_directory(
#     'C:/Users/JUNG1/OneDrive/바탕 화면/이미지유사도/train/posters/',
#     target_size=(224, 224),
#     batch_size=32,
#     class_mode='categorical')

# model.fit(train_generator, epochs=10, steps_per_epoch=len(train_generator))
model.fit(train_data, train_label, epochs=30, batch_size=32)

# 모델 저장
model.save('my_model.h5')

