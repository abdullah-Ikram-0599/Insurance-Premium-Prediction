# Insurance Premium Prediction with CI/CD Deployment

This repository contains an end-to-end machine learning project for predicting insurance premiums. The project utilizes various machine learning models and selects the best-performing model for deployment. It is deployed on AWS Elastic Beanstalk with CI/CD pipelines using AWS CodePipeline. The code is modular, uses logging for easier debugging, and follows best practices for production-grade development.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Model Performance](#model-performance)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Run Locally](#run-locally)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [License](#license)

## Project Overview
This project involves predicting insurance premiums using a dataset obtained from Kaggle. The workflow includes data preprocessing, exploratory data analysis (EDA), model building, and deployment. The best-performing model is selected based on evaluation metrics and deployed using AWS services.

## Features
- Data preprocessing including standardization and encoding
- Model building with Multiple Linear Regression, Decision Tree Regressor, Gradient Boosting, and XGBoost
- Fine-tuning of the best model (XGBoost) using cross-validation
- Deployment on AWS Elastic Beanstalk
- CI/CD pipelines using AWS CodePipeline
- Frontend built with HTML and styled using CSS

## Model Performance
The XGBoost model gave the best performance with an R^2 error of 0.87 after fine-tuning.

## Architecture
The project follows a modular coding approach, which is essential for writing production-grade code. Logging is integrated throughout the codebase to facilitate debugging.

## Setup and Installation

### Clone the Repository
First, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/abdullah-Ikram-0599/Insurance-Premium-Prediction.git
```

### Create a Virtual Environment
Navigate to the project directory and create a virtual environment:
```bash
cd Insurance-Premium-Prediction
python3 -m venv venv
```

### Install Dependencies
Activate the virtual environment and install the required dependencies:
```bash
# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

### Run Locally
Once the dependencies are installed, you can run the application locally:
```bash
python app.py
```

## Usage
1. Navigate to the cloned repository.
2. Create and activate a virtual environment.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Run the application locally using `python app.py`.
5. Open your web browser and go to `http://localhost:5000` to interact with the application.

## Folder Structure
```
Insurance-Premium-Prediction/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── EDA.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `data/`: Contains raw and processed data
- `notebooks/`: Contains Jupyter notebooks for EDA and other analyses
- `src/`: Contains source code for data preprocessing, model training, and prediction
- `templates/`: Contains HTML templates for the frontend
- `static/`: Contains static files like CSS
- `app.py`: Main application file
- `requirements.txt`: List of dependencies
- `README.md`: Project documentation
- `.gitignore`: Git ignore file

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to clone the repository and follow the instructions to set up the project locally. If you encounter any issues or have any questions, please create an issue in the repository. Happy coding!
