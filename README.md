# MachineLearning_DigitRecognition
MachineLearning_DigitRecognition is a neural network trained to perform digit recognition on user drawn digits. Built with Python using PyTorch, Pandas, and Streamlit to create a user interface where digits could be drawn and Plotly to display percent accuracy of the model's digit selections. Run ui.py to run the program.

1. Obtained a training dataset with over 70,000 handwritten digits alongside their actual value from [the MNIST database](https://en.wikipedia.org/wiki/MNIST_database).
2. Divided the dataset into a 6:1 training : test ratio.
3. Flattened the 28X28 image into 784 input nodes.
4. Developed multiple processing layers using [PyTorch](https://pytorch.org/).
5. Created an interactive, graphical frontend using [Streamlit](https://streamlit.io/).

# Use Case
Below is an example of the interface.

![](https://user-images.githubusercontent.com/51927159/235236860-1ae46d54-3e74-4acd-b8f3-8a15b63bfdce.gif)
