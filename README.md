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

This project can be executed using either:
1. Google Colab
2. Local Streamlit Environment

==================================================
☁️ METHOD 1 — RUNNING IN GOOGLE COLAB
==================================================

Step 1 — Upload Files

Upload the following files into Google Colab:

- app.py
- Untitled.ipynb
- HHS_Unaccompanied_Alien_Children_Program (1).csv

--------------------------------------------------

Step 2 — Run the Notebook

Open `Untitled.ipynb` and run all cells.

The required dependencies are already installed inside the notebook code.

--------------------------------------------------

Step 3 — Run Streamlit

Execute:

!streamlit run app.py

--------------------------------------------------

Step 4 — Copy Paste IP into Localhost Link

After running the code, Streamlit generates output similar to:

Local URL: http://localhost:8501  
Network URL: http://172.xx.xx.xx:8501

Copy the generated IP address and paste it into the localhost link if required to access the Streamlit dashboard.

Example:

http://172.xx.xx.xx:8501

Open the generated link in your browser to view the dashboard.

==================================================
💻 METHOD 2 — RUNNING LOCALLY USING STREAMLIT
==================================================

Step 1 — Clone Repository

Open terminal / command prompt and run:

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

Open the URL in your browser to access the dashboard.


