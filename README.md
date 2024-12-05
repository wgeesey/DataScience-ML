# Data Science Files

A collection of data science and machine learning projects I have worked on. These include projects built from tutorials, self-developed models, or ones where I’ve added new functionality.

## Image Prediction
This project uses ImageAI to process image files and make predictions about their content. The current model in use is MobileNetV2, selected for its balance of accuracy and lighter data/storage requirements.

To use a different model, visit ImageAI GitHub, download the desired model package, and update the brain.py file to reflect the new model.

## K-Nearest Neighbor
This folder contains code for implementing the K-Nearest Neighbor (KNN) algorithm with the classic Iris dataset.

- iris_learning: A project where I learned the KNN algorithm, implemented it from scratch, and explored its basics. I also incorporated the Decision Tree model and used Joblib for model persistence.

- iris_elbow: An enhancement to the KNN model, where I added functionality to plot the error rates at various values of k. This helps users evaluate the best value of k based on the plot for optimal results.

### Additional Files
*NumPy and Pandas Cheatsheet: A quick reference with code snippets and comments for working with the NumPy and Pandas libraries.

* Jupyter Notebooks:

  * Iris Notebook: Includes visualizations and serves as a cheat sheet for the Iris dataset, demonstrating basic data analysis and plotting.
  
  * Soccer Notebook: Analyzes and plots data on soccer player wages and values from the FIFA 23 dataset (included as a .csv). This allows a hypothetical General Manager to assess player worth for potential trades or acquisitions.
