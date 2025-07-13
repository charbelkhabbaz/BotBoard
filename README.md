# Insurance-Analytics-Dashboard
**The Insurance Analytics Dashboard** is an interactive Streamlit web application that empowers insurance companies, analysts, and decision-makers to explore and act on policy data in real-time through rich visualizations, integrated machine learning models (for investment prediction, risk analysis, segmentation, anomaly detection, and renewal prediction), and a natural language SQL-based chatbot, all in a single, powerful platform.

**Key Features**
- 📈 Interactive dashboard with filters and KPIs
- 💬 Natural language chatbot for querying database
- 🤖 Machine Learning models:
  - Investment Prediction (Regression , Random Forest Regressor)
  - Risk Classification (Random Forest Classifier)
  - Customer Segmentation (KMeans)
  - Anomaly Detection (Isolation Forest)
  - Renewal Prediction (Logistic Regression)
- 🔗 MySQL backend for real data queries
- 📊 Plotly charts and user-driven insights

**Tech Stack**
- Python
- Streamlit
- scikit-learn
- Pandas, NumPy
- Plotly
- LangChain (for chatbot logic)
- MySQL

**Installation instructions**
**1. Clone the repo**
clone the project
change directory to the project

**2. Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

- Create a MySQL database named `insurance`.
- Run the SQL schema and insert data:
 Provided in myDb.txt file
- Update database credentials in `config.toml` or `.env`:

[mysql]
host = "localhost"
user = "root"
password = "yourpassword"
database = "myDb"

**4. Change the Openrouter API key**
OPENROUTER_API_KEY = "[sk-or-v1-f81251adbad30321d6951ce85a3b488f1e................ Put your api key]"

**5.to Run the Project**
write in the terminal : streamlit run Home.py



- The dashboard loads insurance data from a MySQL table (`insurance`).
- Users can explore the data using dropdown filters and see summaries by region, location, etc.
- The "ML Page" allows users to train and test models:
  
  -Users select ML task from a dropdown (investment prediction, risk analysis, etc.)
  
  -Models are trained using scikit-learn with visual feedback (feature importance, MSE, etc.)
- The chatbot uses a SQL generator (LangChain or custom parser) to convert natural language to SQL queries and return real results from the DB than convert back the response to a human friendly language.

 🧾 Dashboard Overview
This is the main page of the dashboard, where users can interact with the insurance dataset in **REAL TIME**.
A "View Dataset" section allows users to explore the full table stored in the MySQL database.
Users can filter the data dynamically by:
Region/Location/Construction type/Specific columns

🟡 Important: All visualizations and charts in the dashboard are automatically updated based on the filters applied, not just the table view.
⚡ Real-Time Data:
The dashboard fetches data live from the MySQL database using SQL queries. If any data in the database is updated, the dashboard reflects the changes.

<img width="1566" height="777" alt="Capture1" src="https://github.com/user-attachments/assets/7fffc5f4-904d-462d-b88d-d52f58955e3f" />


<img width="1542" height="773" alt="Capture2" src="https://github.com/user-attachments/assets/a8239224-4949-4c38-8aaa-69549cb4fce2" />


<img width="1577" height="775" alt="Capture3" src="https://github.com/user-attachments/assets/2d3c6f06-adf6-4e85-a19f-bc6e82049337" />

The Progress page displays the target investment and shows how close the business’s total investment is to the specified target.

<img width="1577" height="674" alt="Capture4" src="https://github.com/user-attachments/assets/17713e6e-474b-41df-96a3-6095efca88d1" />

🤖 **Machine Learning Page Overview**
The Machine Learning page provides access to multiple predictive models that analyze the insurance data from different perspectives, including:

**Machine Learning Models Used:**
1. 📈 Investment Prediction
Linear Regression: Simple linear model for predicting investment amounts
Random Forest Regressor: Ensemble model with 100 estimators for more complex investment predictions
2. 🎯 Risk Analysis
Random Forest Classifier: Binary classification model to identify high-risk vs low-risk policies
Uses features: Investment amount and calculated Risk Score
Risk Score = average of (Earthquake, Flood, Rating features)
3. 👥 Customer Segmentation
K-Means Clustering: Unsupervised clustering algorithm
Configurable number of segments (2-6 clusters)
Uses features: Investment and Rating
Standardizes features with StandardScaler before clustering
4. 🔍 Anomaly Detection
Isolation Forest: Unsupervised anomaly detection algorithm
Configurable contamination rate (1-10%)
Uses features: Investment, Rating, Earthquake, Flood
Standardizes features with StandardScaler
5. 🔄 Renewal Prediction
Logistic Regression: Binary classification for predicting policy renewal likelihood
Uses features: Investment, Rating, Days to Expiry
Creates synthetic renewal data based on Rating scores


<img width="1576" height="719" alt="Capture5" src="https://github.com/user-attachments/assets/d0f51d70-f798-420b-8cb1-4babf84826fc" />


<img width="1557" height="698" alt="Capture6" src="https://github.com/user-attachments/assets/98c9cb89-b8e4-4e25-a75f-7107bec9130b" />

💬 Chatbot Integration
The chatbot is designed to simplify interaction with the insurance dataset by allowing users to ask any natural language question related to the data. It connects to the MySQL database (myDb) and works by understanding the user's question, converting it into an SQL query, executing it, and then transforming the result back into a natural language response. The answer is presented in two formats: one for non-technical users, where the response is explained in clear, understandable terms with helpful context; and one for technical users, where the chatbot also shows the exact SQL query used to retrieve the answer. This dual output makes the chatbot both user-friendly and developer-friendly, bridging the gap between business users and technical professionals.
This makes the chatbot both user-friendly and developer-aware, bridging the gap between business users and technical professionals.


<img width="1547" height="689" alt="Capture7" src="https://github.com/user-attachments/assets/3fc12349-f7a3-45c6-96ca-dc9b009ed666" />


<img width="1540" height="696" alt="Capture8" src="https://github.com/user-attachments/assets/6c654cd8-dc11-4f5b-83b0-6b903cad6bef" />


<img width="1574" height="758" alt="Capture9" src="https://github.com/user-attachments/assets/31ad7f8d-64ce-4ac1-917e-c99f592a3490" />
