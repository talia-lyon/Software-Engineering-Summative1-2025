# User Documentation for Risk Assessment Dashboard

## Introduction
The Risk Assessment Dashboard is an interactive web-based tool designed for supervisory teams to assess financial risks effectively. It enables users to upload datasets, analyse high-level metrics, and explore risk data through visualisations. This document provides guidance on using the dashboard.

---

## Getting Started

### Accessing the Dashboard
1. Open the application in your browser at the following URL:
   - If running locally: 
     1. Clone the repository:
        ```bash
        git clone <https://github.com/talia-lyon/Software-Engineering-Summative1-2025.git>
        cd 
        ```
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

2. The dashboard has three primary tabs available via the sidebar:
   - **Overview**: View high-level insights.
   - **Upload Data**: Upload your dataset or use the default dataset.
   - **Risk Visualisations**: Explore detailed visualisations for risk analysis.

---

## Features

### Overview Tab
- **Purpose**: Display summary metrics and high-level visualisations.
- **Instructions**:
  - View key financial metrics (e.g., Average Risk Score, Liquidity Ratio).
  - Examine the two high-level visualisations that summarise trends in the data.

---

### Upload Data Tab
- **Purpose**: Upload a custom dataset or use the provided default dataset.
- **Instructions**:
  1. **Use Default Dataset**:
     - Click the `Use Default Dataset` button to load pre-existing data.
     - The default dataset preview will appear below the button.
  2. **Upload Your Dataset**:
     - Click the `Choose File` button to select a `.csv` file from your computer.
     - Click the `Preview Data` button to view the uploaded dataset.
     - Click the `Upload` button to upload the dataset 
  - Ensure the dataset adheres to the expected format (e.g., appropriate columns such as `Company`, `Risk Score`, `Liquidity Ratio`).

---

### Risk Visualisations Tab
- **Purpose**: Explore interactive visualisations for a deeper understanding of risk metrics.
- **Instructions**:
  - Bar Chart:
    - Displays risk scores by company.
    - Hover over bars for additional information.
  - Scatter Plot:
    - Shows liquidity ratios vs risk scores.
    - Use zoom and pan controls for detailed analysis.

---

### Help Modal
- **Purpose**: Provides contextual guidance on using the dashboard.
- **Instructions**:
  - Click the `Show Help` button located in the top-right corner.
  - Read the instructions for the current tab or feature.

---

## Troubleshooting

1. **File Upload Issues**:
   - Ensure the file is in `.csv` format.
   - Verify the dataset includes all required columns (e.g., `Risk Score`, `Liquidity Ratio`).

2. **Visualisation Errors**:
   - Check for invalid or missing data values in your dataset.

---

## Contact
For further assistance, contact [Talia Lyon] at [lyon.t@northeastern.edu].
