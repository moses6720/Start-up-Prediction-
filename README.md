# 🚀 Startup Success Prediction using Machine Learning

A Machine Learning project that predicts whether a startup is likely to succeed or fail based on business fundamentals such as funding, team strength, market size, and revenue.

This project uses **Random Forest Algorithm** and provides predictions through an interactive **Streamlit Web Application**.

---

# 📌 Project Objective

The objective of this project is to build a prediction system that estimates startup success probability using historical business data.

The model analyzes important factors such as:

- Funding rounds
- Founder experience
- Team size
- Market size
- Product users
- Revenue
- Burn rate
- Investor type
- Sector
- Founder background

The system predicts whether a startup is likely to:

✔ Succeed (IPO or Acquisition)  
❌ Fail

---

# 🧠 Machine Learning Approach

### Algorithm Used
Random Forest Classifier

### Why Random Forest?

- High accuracy
- Handles structured data well
- Reduces overfitting
- Works with both categorical and numerical data
- Provides feature importance ranking

---

# 📊 Dataset Information

Dataset contains startup business details with the following columns:

| Feature | Description |
|--------|-------------|
| funding_rounds | Number of investment rounds |
| founder_experience_years | Founder experience |
| team_size | Number of employees |
| market_size_billion | Market size in billion USD |
| product_traction_users | Number of users |
| burn_rate_million | Company expenses |
| revenue_million | Company revenue |
| investor_type | Type of investor |
| sector | Business industry |
| founder_background | Founder education |
| outcome | IPO / Acquisition / Failure |

---

# ⚖ Why Dataset Balancing was Required

Original dataset had imbalance:

Failure > Success

Machine learning models become biased toward majority class.

We balanced dataset using resampling technique so that:

Success cases = Failure cases

This improves prediction fairness and accuracy.

---

# 🏗 Project Workflow

1. Data Collection
2. Data Cleaning
3. Feature Selection
4. Data Balancing
5. Model Training
6. Model Evaluation
7. Prediction System
8. Web App Deployment

---

# 📈 Model Performance

Evaluation metrics used:

- Accuracy Score
- Confusion Matrix
- Classification Report

Example Accuracy:

82%

---

# 📊 Feature Importance Graph

Important factors affecting startup success:

- Revenue
- Market size
- Product users
- Team size
- Founder experience

(Add graph screenshot here)

Example file name:

images/feature_importance.png

---

# 📉 Correlation Heatmap

Shows relationship between different features.

(Add heatmap screenshot here)

Example file name:

images/heatmap.png

---

# 💻 Streamlit Web Application

User enters startup details through web interface.

Model predicts:

Startup success probability.

---

# 🖥 Example Input

Funding Rounds: 7  
Team Size: 45  
Founder Experience: 12 years  
Market Size: 30 billion  
Users: 900000  
Revenue: 20 million  
Burn Rate: 3 million  
Investor Type: VC  
Sector: AI  
Founder Background: Technical  

---

# 📊 Example Output

Startup likely to SUCCEED

Success Probability: 84%

(Add output screenshot here)

Example file name:

images/output.png

---

# 🛠 Technologies Used

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
Seaborn  
Streamlit  
Pickle  

---

# 📂 Project Structure


ML_Startup/
│
├── main.ipynb
├── app.py
├── model.pkl
├── model_columns.pkl
├── startup_success_dataset.csv
│
├── images/
│ ├── heatmap.png
│ ├── feature_importance.png
│ ├── output.png
│
└── README.md


---

# ▶ How to Run Project

### Step 1 Install libraries


pip install pandas numpy matplotlib seaborn scikit-learn streamlit


### Step 2 Train model

Run notebook:


main.ipynb


### Step 3 Run Streamlit app


streamlit run app.py


---

# 🎯 Applications

Startup evaluation  
Investment decision support  
Business analytics  
Machine learning learning project  

---

# 🔮 Future Improvements

Use real-world dataset  
Add deep learning model  
Deploy application online  
Improve UI design  
Add financial indicators  

---
