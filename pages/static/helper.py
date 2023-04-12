import streamlit as st
import tensorflow as tf
from PIL import ImageOps, Image
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
import os
import h5py


def prediction(image):
    classifier = load_model('pages/static/imageclassifier.h5')
    shape = ((226, 226, 3))
    test_image = image.resize((256, 256))
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image/255.0
    test_image = np.expand_dims(test_image, axis=0)
    prediction = classifier.predict(test_image)
    labels = ['Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Potato___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight', 'Tomato___Septoria_leaf_spot', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Strawberry___Leaf_scorch', 'Peach___healthy', 'Apple___Apple_scab', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 'Apple___Black_rot', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
              'Peach___Bacterial_spot', 'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Pepper,_bell___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy', 'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles)', 'Raspberry___healthy', 'Tomato___Leaf_Mold', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Pepper,_bell___Bacterial_spot', 'Corn_(maize)___healthy']
    return np.argmax(prediction[0])  # labels[np.argmax(prediction[0])]


def tips():
    return """1.Use quality seeds: Make sure to use high-quality seeds to start your crops. Healthy seeds have better resistance to pests and diseases and will help ensure a strong start for your crops.

2.Soil health: Good soil health is essential for healthy crops. Make sure the soil has adequate nutrients, pH level, and organic matter. You can also add compost or fertilizer to enrich the soil.

3.Watering: Water the crops regularly, but don't overwater. Most crops need around an inch of water per week. Make sure the water is evenly distributed, and avoid watering during the hottest part of the day.

4.Mulching: Mulching helps to retain moisture in the soil, suppress weed growth, and keep the soil temperature even. Use organic materials like straw or leaves for best results.

5.Crop rotation: Rotating crops helps to prevent the build-up of pests and diseases in the soil. Rotate your crops every year, alternating between different plant families.

6.Pest control: Use natural methods to control pests, such as companion planting, insect-repelling herbs, and natural insecticides. Avoid using harmful chemicals that can harm the environment and the crops.

7.Weed control: Weeds can compete with crops for nutrients, water, and sunlight. Remove weeds regularly using hand weeding, hoeing or mulching.

8.Pruning: Prune your crops regularly to remove dead or diseased parts. This will help prevent the spread of diseases and improve air circulation around the plants.

9.Sunlight: Ensure that your crops receive adequate sunlight. Most crops require at least six hours of sunlight per day. Choose a spot that receives the most sunlight for planting.

10.Observation: Observe your crops regularly for signs of pests, diseases, or nutrient deficiencies. This will help you catch any problems early and take corrective action before they get worse."""