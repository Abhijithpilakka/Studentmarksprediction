# Student Mark Prediction Project

## Overview

The Student Mark Prediction project is an end-to-end machine learning application that predicts student marks based on historical data. The project involves data preprocessing, model training, and deployment as a web application on the Azure cloud platform.

## Features

- Ingestion and Transformation Pipelines: The project implements robust data pipelines for ingesting and transforming raw data into a format suitable for model training. This ensures data quality and consistency throughout the process.

- Multiple Regression Models: Various regression algorithms such as Linear Regression, Decision Tree Regression, and Random Forest Regression are utilized to predict student marks. This diversity allows for model comparison and selection based on performance metrics.

- Scalable Deployment: The trained model is deployed as a web application on the Azure cloud using Azure Machine Learning and Azure App Service. This provides users with an accessible and responsive interface to input student information and receive mark predictions in real-time.

- User-Friendly Interface: The web application includes an intuitive user interface that allows users to input relevant student details. The application then presents predicted marks, providing a seamless experience for users.

## Technologies Used

- Python
- pandas
- scikit-learn
- flask
- Azure App Service

## Project Structure

The project is organized into the following components:

- `data_ingestion.py`: Contains code for data ingestion from various sources and initial preprocessing steps.
- `data_transformation.py`: Implements data transformation and feature engineering to prepare data for model training.
- `model_training.py`: Includes code for training multiple regression models using different algorithms.
- `app.py`: This directory holds the web application code, including the UI and integration with the trained model.
- `Templates`: Webapp structure.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the data ingestion and transformation pipelines using `python data_ingestion.py` and `python data_transformation.py`.
4. Train the regression models using `python model_training.py`.
5. Navigate to the `webapp` directory and follow the instructions in its README to deploy and run the web application locally or on Azure.

## Credits

This project was developed by Abhijith as a demonstration of machine learning, data engineering, and cloud deployment skills.
THanking Krish Naik for his step by step guide on building end to end ML projects.

## Screenshots

![image](https://github.com/Abhijithpilakka/Studentmarksprediction/assets/71208534/d9aec2ef-ef2d-4b39-bb6f-ed9210e23d1a)


