# 📊 Care Transition Efficiency & Outcome Analytics

An interactive Streamlit dashboard and analytical study focused on evaluating the operational efficiency of the U.S. Department of Health and Human Services (HHS) Unaccompanied Children (UAC) care pipeline.

This project models the UAC system as a dynamic care transition pipeline and analyzes how efficiently children move through different stages of care — from CBP custody to HHS care and finally to sponsor placement.

---

# 🧠 Project Overview

Most traditional reporting systems focus only on how many children are currently in custody or care. However, this project shifts the focus toward:

- Process efficiency
- Transition speed
- Backlog accumulation
- Outcome stability
- Operational bottlenecks

Instead of asking:

> “How many children are currently in the system?”

this project asks:

- How efficiently are children transferred?
- Are discharges keeping pace with intake?
- Where are delays happening?
- Is the system recovering over time?

---

# 📁 Project Structure


care-transition-analytics-for-alien-children/
│
├── app.py
├── analysis.ipynb
├── HHS_Unaccompanied_Alien_Children_Program (1).csv
├── requirements.txt
└── README.md


# 🚀 Running the Project

This project can be executed using three different methods:

1. Direct Streamlit Cloud Access (Easiest Method)
2. Google Colab
3. Local Streamlit Environment

==================================================
🌐 METHOD 1 — DIRECT STREAMLIT CLOUD ACCESS
(EASIEST METHOD)
==================================================

Step 1 — Open the GitHub Repository

Open the GitHub repository and click the Streamlit App link provided in the repository description or README file.

Example:

https://care-transition-analytics-for-alien-children-fz4bjnuzygv95kfgr.streamlit.app/

--------------------------------------------------

Step 2 — Access Dashboard

The Streamlit dashboard will open directly in your browser.

No installation or setup is required.

--------------------------------------------------

Step 3 — Explore Dashboard Features

The dashboard includes:

- Care Pipeline Visualization
- Transfer Efficiency Analysis
- Discharge Effectiveness Tracking
- Peak Backlog Detection
- Outcome Stability Monitoring
- Weekday vs Weekend Analysis
- Threshold-Based Alert System

==================================================
☁️ METHOD 2 — RUNNING IN GOOGLE COLAB
==================================================

Step 1 — Upload Files

Upload the following files into Google Colab:

- app.py
- analysis.ipynb
- healthcare uac (1).csv

--------------------------------------------------

Step 2 — Run the Notebook

Open `analysis.ipynb` and run all cells.

The dependencies are already installed inside the notebook code.

--------------------------------------------------

Step 3 — Run Streamlit

Execute:

!streamlit run app.py

--------------------------------------------------

Step 4 — Open Dashboard

After execution, Streamlit automatically generates:

- Local URL
- Network URL
- External URL

Copy and paste the External URL into your browser to access the dashboard.

==================================================
💻 METHOD 3 — RUNNING LOCALLY USING STREAMLIT
==================================================

Step 1 — Clone Repository

git clone https://github.com/your-username/care-transition-analytics.git

--------------------------------------------------

Step 2 — Move Into Project Folder

cd care-transition-analytics

--------------------------------------------------

Step 3 — Install Dependencies

pip install -r requirements.txt

--------------------------------------------------

Step 4 — Run Streamlit Dashboard

streamlit run app.py

--------------------------------------------------

Step 5 — Open Dashboard

After execution, Streamlit automatically generates:

http://localhost:8501

Copy and paste the localhost URL into your browser to access the dashboard.

==================================================
📦 requirements.txt
==================================================

streamlit
pandas
plotly
numpy
pyngrok


