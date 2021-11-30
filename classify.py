from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, array_to_img
import numpy as np
import streamlit as st
from keras.preprocessing.image import img_to_array
from skimage import transform


@st.cache(allow_output_mutation=True)
def get_model():
    cnn = load_model('tumor_model.h5')
    # print('Model Loaded')
    return cnn


def predict(image_data):
    loaded_model = get_model()
    img = img_to_array(image_data)
    np_image = transform.resize(img, (64, 64, 3))
    image4 = np.expand_dims(np_image, axis=0)
    result__ = loaded_model.predict(image4)
    return result__


def get_mod_sum():
    with st.expander("See Model Summery"):
        st.write("")
        st.image("model_summery.png")
