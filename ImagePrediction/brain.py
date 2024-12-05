# Import the ImageClassification class from the updated ImageAI library
# The old `imageai.Prediction` module has been replaced with `imageai.Classification`
from imageai.Classification import ImageClassification
import os

# Set the execution path to the current working directory
# This helps in dynamically locating models or input files relative to the script location
exec_path = os.getcwd()

# Initialize the ImageClassification object for performing image classification
prediction = ImageClassification()

# Specify the model type to use; SqueezeNet is no longer supported
# MobileNetV2 is now one of the fastest models provided by ImageAI
prediction.setModelTypeAsMobileNetV2()

# Set the path to the pre-trained MobileNetV2 model file
# Ensure the model file (mobilenet_v2-b0353104.pth) is downloaded and placed in the current directory
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))

# Load the specified model into memory for classification
prediction.loadModel()

# Perform image classification on the specified image (house.jpg)
# `result_count=5` limits the output to the top 5 predictions
predictions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, 'godzilla.jpg'), 
    result_count=5
)

# Loop through predictions and their corresponding probabilities
# Print each class label (prediction) with its confidence percentage (probability)
for eachPred, eachProb in zip(predictions, probabilities):
    print(f'{eachPred} : {eachProb}')
