# Technical Documentation for Risk Assessment Dashboard

## Introduction
The Risk Assessment Dashboard is built using Flask for backend functionality, HTML/CSS for front-end structure, and Plotly for interactive visualisations. This document provides an overview of the architecture, workflow, and key technical details.

---

## Project Structure

risk-assessment-dashboard/

├── app/

│   ├── __init__.py          # Application factory and configuration

│   ├── routes.py            # Flask routes for handling requests

│   ├── templates/           # HTML templates for rendering views

│   │   ├── index.html       # Overview tab layout

│   │   ├── upload.html      # Upload Data tab layout

│   │   ├── visualisations.html # Risk Visualisations tab layout

│   ├── static/              # Static assets (CSS, JavaScript)

│   │   ├── styles.css       # Dashboard styling

│   │   ├── scripts.js       # Client-side interactivity

├── uploads/                 # Directory for storing uploaded datasets

├── docs/                    # Documentation (user and technical guides)

│   ├── user_documentation.md   # User instructions for the dashboard

│   ├── technical_documentation.md # Technical details for developers

├── requirements.txt         # Python dependencies

├── run.py                   # Entry point to run the Flask application

├── README.md                # Project overview and usage instructions


---

## Technical Workflow

### 1. Data Upload
- Users can upload a `.csv` file via the `Upload Data` tab.
- The file is stored in the `uploads/` directory for processing.
- Uploaded data is validated for format and schema consistency.

### 2. Data Processing
- The dataset is loaded into a Pandas DataFrame for manipulation.
- Validation checks include:
  - Ensuring all required columns (e.g., `Risk Score`, `Liquidity Ratio`) are present.
  - Removing null or invalid entries.

### 3. Visualisation
- Processed data is passed to Plotly to generate interactive charts.
- Bar charts and scatter plots are created dynamically based on user-uploaded or default datasets.

### 4. Error Handling
- Invalid file uploads trigger error messages displayed on the UI.
- Issues with missing data are logged and displayed to the user.

---

## Flask Routes
- `/` (GET): Serves the `Overview` page with summary metrics and visualisations.
- `/upload` (POST): Handles file uploads and displays a preview of the dataset.
- `/visualisations` (GET): Displays interactive visualisations based on the data.

---

## Dependencies
- **Flask**: Web framework for routing and backend logic.
- **pandas**: Data processing and manipulation.
- **Plotly**: Dynamic, interactive visualisations.
- **Bootstrap**: Frontend framework for responsive design.

---

## Deployment Instructions

### Local Deployment
1. Clone the repository:
   ```bash
        git clone <https://github.com/talia-lyon/Software-Engineering-Summative1-2025.git>
2. Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```
3. Start the Flask application:
   ```bash
   python run.py
   ```
4. Open the application in your browser:
   - Navigate to `http://127.0.0.1:5000`.

### Production Deployment
- Use a platform like Heroku, AWS, or Docker to host the application.
- Configure the application for production-level scaling and security.

---

## Data Validation
- Ensure uploaded datasets are in .csv format with the following schema:
  - Columns:
    - Company: String.
    - Risk Score: Numeric (0–100).
    - Liquidity Ratio: Numeric (non-negative).
  - Missing Data: Remove rows with null or invalid values.

---

## Future Improvements
1. Add role-based access control for secure multi-user access.
2. Implement database integration to persist datasets and user configurations.
3. Optimise data processing for large datasets.
4. Include additional visualisation types (e.g., line charts, heatmaps).

---

## Contact
For further assistance, contact [Talia Lyon] at [lyon.t@northeastern.edu].