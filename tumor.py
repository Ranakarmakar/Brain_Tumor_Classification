import streamlit as st
from PIL import Image
import classify
import time

st.set_page_config(layout="wide", page_title="Brain Tumor", page_icon="Brain")

st.title("Brain Tumor Classification")
c1, c2 = st.columns(2)
with c1:
    uploaded_file = st.file_uploader("Choose MRI Image..", accept_multiple_files=False)

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        if st.button('   Submit  '):
            result = classify.predict(image)
            with st.spinner('Loading Result...'):
                time.sleep(2)
            st.subheader("Result")
            if result[0][0] == 1:
                prediction = 'Warning!!! Tumor is Cancerous, Please Consult to Your Doctor'
                st.error(prediction)
                classify.get_mod_sum()
            else:
                prediction = "It's a Normal Tumor. Please Consult to Your Doctor."
                st.success(prediction)
                classify.get_mod_sum()


with c2:
    if uploaded_file is not None:
        st.image(uploaded_file)
    else:
        st.markdown("Brain tumour is a very serious brain cancer. It is present or become due to the separation of "
                    "the brain cells. In the recent field of this study, tells us that deep learning will help in "
                    "health industry of medical diseases imaging in the Medical Diagnostic of all the diseases. So, "
                    "I built this Application for Practice Purpose and suggesting to Consult to Your Doctor.")
c3, c4 = st.columns(2)
with c3:
    st.header("")
h1, h2, h3 = st.columns([1, 4, 1])
with h2:
    if uploaded_file is None:
        st.header("")
    # st.download_button()

d1, d2, d3 = st.columns(3)
with d1:
    with open("yes_or_no.jpg", "rb") as file:
        btn = st.download_button(
            label="Download Sample MRI Image",
            data=file,
            file_name="yes_or_no.jpg",
            mime="image/png"
        )

# Conclusion
ex1, ex2, ex3 = st.columns(3)
with ex1:
    with st.expander("About The Project"):
        st.markdown("Brain Tumor Classification")
        st.markdown(
            "The human brain is the major controller of the humanoid system. The abnormal growth and division of cells "
            "in the brain lead to a brain tumor, and the further growth of brain tumors leads to brain cancer. In the "
            "area of human health, Computer Vision plays a significant role, which reduces the human judgment that "
            "gives accurate results. CT scans, X-Ray, and MRI scans are the common imaging methods among magnetic "
            "resonance imaging (MRI) that are the most reliable and secure. MRI detects every minute objects. Our "
            "paper "
            "aims to focus on the use of different techniques for the discovery of brain cancer using brain MRI. In "
            "this study, we performed pre-processing using the bilateral filter (BF) for removal of the noises that "
            "are "
            "present in an MR image. This was followed by the binary thresholding and Convolution Neural Network (CNN) "
            "segmentation techniques for reliable detection of the tumor region. Training, testing, and validation "
            "datasets are used. Based on our machine, we will predict whether the subject has a brain tumor or not. "
            "The "
            "resultant outcomes will be examined through various performance examined metrics that include accuracy, "
            "sensitivity, and specificity. It is desired that the proposed work would exhibit a more exceptional "
            "performance over its counterparts.")
with ex3:
    with st.expander("About Developer"):
        st.markdown("Rana Karmakar")
        st.write("I have a deep interest in Artificial Intelligence and Machine Learning ever since I got to know "
                 "about it; the sci-fi films, comics and stories have always fascinated me. I love to learn new "
                 "skills to keep myself up-to-date with the corporate world. I believe in maintaining a work-life "
                 "balance while learning and working upon different fields of interest.I have had a taste of many "
                 "different technologies: creating Websites, Software Development, Data Analysis, "
                 "creating Machine Learning models, Cloud Computing and Developing complex programs and more. "
                 "Feel free to give Feedback at ranakarmakar027@gmail.com")
with ex2:
    with st.expander("Contact"):
        st.markdown("ranakarmakar027@gmail.com")
        st.write("[LinkedIn](https://www.linkedin.com/in/rana-karmakar-0972641a6)")
        st.write("Other Apps[Movie Recommendation System]("
                 "https://share.streamlit.io/ranakarmakar/streamlit_movie_recommendation/main/app.py)")


