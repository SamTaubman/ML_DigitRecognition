import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import torch
import torchvision.transforms as T
import torch.nn.functional as F
from recognition import transform_image, prediction
import pandas as pd
import plotly.graph_objects as go
import gc

#Enable garbage collection
gc.enable()

def main():
    st.set_page_config(page_title="Handwritten Digit Recognition", initial_sidebar_state="expanded")
    st.title('Digit Recognizer')
    st.write("Have a neural network recognize any digit you write!")
    st.markdown('### Draw a digit !')

    st.sidebar.header("Configuration")
    stroke_width = st.sidebar.slider("Brush width: ", 10, 30, 20)
    drawing_mode = st.sidebar.checkbox("Drawing mode ?", True)


# To plot classes and probabilitites
def plot_figure(df):

    fig = go.Figure(go.Bar(
    x=df[0].tolist(),
    y=list(df.index),
    orientation='h'))

    fig.update_yaxes(type='category')

    # Label axes and title, center the title, change fonts 
    fig.update_layout(    
        title={
                'text': "Classes vs Probabilities",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
        xaxis_title="Probabilities",
        yaxis_title="Classes",
        font=dict(
            family="Courier New, monospace",
            size=18,
            # color="RebeccaPurple"
            ))

    st.plotly_chart(fig)

    del fig


SIZE = 256
canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=stroke_width,
    stroke_color='#FFFFFF',
    background_color='#000000',
    width=SIZE,
    height=SIZE,
    drawing_mode="freedraw" if drawing_mode else "transform",
    key='canvas')

if canvas_result.image_data is not None:

    # cv2 METHOD
    # nd_array -> resized nd_array -> grayscale nd_array -> pytorch tensor

    # Resize the image to 28x28 for the model input
    img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
    # Rescaling the image just to view the model input clearly 
    rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST) 
    st.write('`Model input (rescaled)`')
    st.image(rescaled)


    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Convert to Pytorch Tensor
    tensor_img = transform_image(img_gray)


    clicked = st.button('Run')

    if clicked:

        with st.spinner(text='In progress'):
            image_transformed = transform_image(img_gray)
            class_label , confidence, probs = prediction(image_transformed)

        st.info('Run Successful !')

        if confidence > 50:
            st.write('### `Prediction` : ', str(class_label))
            st.write('### `Confidence` : {}%'.format(confidence)) 
            st.write('&nbsp') # new line
            st.write('**Probabilities**')
            df = pd.DataFrame(probs.numpy())
            st.dataframe(df)
            df = df.transpose()
            plot_figure(df)

           

            del img_gray, image_transformed , class_label, confidence, df 

        else:
            st.write('### `Prediction` : Unable to predict')
            st.write('### `Confidence` : {}%'.format(confidence)) 
            st.write('&nbsp') # new line
            st.write('**Probabilities**')
            df = pd.DataFrame(probs.numpy())
            st.dataframe(df)
            df = df.transpose()
            plot_figure(df)
            del img_gray, image_transformed , class_label, confidence, df

gc.collect()

if __name__ == "__main__":
    main()
