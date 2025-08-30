😃 World Happiness Rank Predictor
This project is a machine learning application that predicts the World Happiness Rank of a country based on six key socio-economic factors. The prediction is made using a Random Forest Regressor model trained on the World Happiness Report dataset spanning from 2015 to 2019.

The application features an interactive web interface built with Gradio, allowing users to adjust the input factors and see the predicted happiness rank in real-time.

Live Demo & Screenshot
Live Link:
A temporary live, shareable link will be generated in your terminal when you run the application. It will look something like this:
Running on public URL: https://xxxxxxxx.gradio.live

Application UI:

🚀 Features
Interactive Predictions: Sliders for six input factors update the prediction instantly.

Real-time Visualization: A bar chart visualizes the contribution of each factor.

Qualitative Feedback: The predicted rank is accompanied by a descriptive label (e.g., "Very High 😊", "Medium 😐").

Professional UI: A clean, modern, and responsive interface built with Gradio.

Data-Driven: The model is trained on 5 years of consolidated happiness data.

🛠️ Tech Stack
Backend: Python

Machine Learning: Scikit-learn, Pandas, NumPy

Web Framework / UI: Gradio

Data: World Happiness Report (2015-2019)

⚙️ Setup and Installation
To run this project locally, follow these steps:

Clone the repository:

git clone <your-repository-url>
cd <your-repository-directory>

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:
Create a requirements.txt file with the following content:

pandas
numpy
scikit-learn
gradio

Then, install the packages:

pip install -r requirements.txt

Ensure necessary files are present:
Make sure the following files are in the root directory:

best_model.pkl (the trained model)

combined_happiness_data.csv (the dataset)

app.py (the Gradio application)

▶️ How to Run
Launch the Gradio application by running the app.py script from your terminal:

python app.py

The application will start, and you can access it at the local URL provided (e.g., http://127.0.0.1:7860).

📊 Data Analysis & Visualizations
The exploratory data analysis (EDA) and model validation revealed several key insights.

1. Correlation Matrix of Features
A heatmap was generated to understand the correlations between different variables. As expected, factors like Economy, Health, and Family (Social Support) show a strong positive correlation with a better (lower) Happiness Rank.

2. Feature Importance
The trained Random Forest model allowed us to evaluate the importance of each feature in determining the happiness rank. Economy (GDP per Capita) and Health (Life Expectancy) were identified as the most significant predictors.

🤖 The Model
The prediction model is a Random Forest Regressor. This ensemble model was chosen after evaluating several regression algorithms. It provided a high R-squared value and robust performance on the validation set, making it well-suited for this prediction task.

📁 Project Structure
.
├── 📄 app.py                     # Main Gradio application script
├── 📄 best_model.pkl               # Trained machine learning model
├── 📄 combined_happiness_data.csv    # Consolidated dataset (2015-2019)
├──  notebooks/
│   ├── 📄 combine.ipynb              # Notebook for data combination
│   ├── 📄 data-visualization.ipynb   # Notebook for EDA and plots
│   ├── 📄 eda.ipynb                  # Initial exploratory data analysis
│   └── 📄 model_validation.ipynb     # Notebook for model training and evaluation
└── 📄 README.md                  # This file
