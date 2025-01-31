# Software Engineering Summative 1

# Risk Assessment Dashboard

## Introduction
The Risk Assessment Dashboard is a web-based tool designed to streamline the process of assessing financial risks for 
supervisory teams. Built using Flask, HTML, and Plotly for interactive visualisations, the dashboard provides a platform 
for uploading datasets, viewing key metrics, and analysing risks through graphical representations. This aligns with best 
practices in software engineering, such as modular design and usability, as emphasised by Sommerville (2016). Furthermore, 
by incorporating interactive visualisations, the application adheres to principles of effective data communication 
outlined by Knaflic (2015), supporting decision-making in regulatory environments with actionable insights.

---

## Features
1. **Overview Tab**:
   - Displays a summary of high-level metrics and visualisations to provide a quick snapshot of financial risks.
2. **Upload Data Tab**:
   - Allows users to upload custom datasets in CSV format or use a default dataset.
   - Provides a preview of the uploaded or default dataset.
3. **Risk Visualisations Tab**:
   - Offers interactive visualisations, such as bar charts and scatter plots, to analyse risk scores and liquidity ratios.
4. **Help Modal**:
   - A built-in help system provides users with guidance on navigating and using the dashboard.

---

## Project Planning

### Project Management Tools

- **GitHub Projects**:
  - The project utilised GitHub Projects to manage tasks efficiently through a Kanban board, breaking down features into 
  manageable user stories like "File Upload" and "Generate Visualisations." This approach follows agile methodologies, 
  which are considered a gold standard in iterative development (Schwaber and Sutherland, 2020). 
  - Milestones were set fortasks such as basic data upload and advanced filtering, ensuring timely delivery. 
  - Regular commits provided version control and traceability of changes, a practice that aligns with Royce’s (1987) recommendations for managing software
  systems.

| ![Example User Story](images/example%20user%20story.png) | ![Kanban Board](images/kanban.png) |
|----------------------------------------------------------|--------------------------------------------|
| Example of User Story 1                                  | Kanban Board                               |

- **Milestones**:
  - Specific milestones were defined to track progress, including:
    - Sprint 1: Basic Data Upload and Preview
    - Sprint 2: Basic Visualisations 
    - Sprint 3: Advanced Filtering and Metrics
    - Sprint 4: Polish and Help Section
  - Each milestone had clear deadlines and measurable goals, ensuring timely delivery of features.

![Milestones](images/milestones.png)

### Iterative Development

- The project followed an **iterative approach**, where features were developed incrementally and refined based on feedback. For example:
  - Initial designs in Figma were reviewed before being translated into functional tabs.
  - Visualisations were initially static but iterated upon to include interactive functionality using Plotly.

### Lessons Learned

- **Effective Sprint Planning**: Breaking down the project into smaller tasks and setting milestones helped avoid scope creep.
- **Collaboration with GitHub**: Using GitHub for version control and project tracking streamlined communication and task management.
- **Continuous Improvement**: The iterative approach allowed for regular feedback, ensuring the final product met user requirements.

---

## Design Phase
### Figma Design
Below is the initial design created in Figma, illustrating the layout and functionality of the dashboard:

![Figma Design](images/figma-1.png)

The design includes:
- **Sidebar Navigation**: Tabs for navigating between Overview, Upload Data, and Risk Visualisations.
- **Key Metrics Section**: Displaying three key financial metrics.
- **Overview Visualisations**: Space allocated for two high-level visualisations.

### Tabs and Screenshots
Each tab is designed to fulfil specific functionality. Below are the screenshots of their final implementations and the
previous iterations they went through:

#### Overview Tab
- **Purpose**: Provides a summary of high-level metrics and visualisations.

- **Development:** This page went through a few iterations to achieve a design similar in look to that of my Figma design 
above. To begin with, I created a design with the colours and basic homepage design. Then, I added the 
tabs, 'company logo', and grid of where the metrics and visualisations would be. The final iteration closely resembles my
Figma design.

| ![First Iteration of Overview](images/3.png)  | ![Overview Tab](images/final%20static.png) |
|-----------------------------------------------|--------------------------------------------|
| First Iteration of Overview Tab (with colour) | Overview Tab                               |


- **Features**:
  - Key metrics displayed in cards.
  - Two high-level visualisations summarising risk trends.

#### Upload Data Tab
- **Purpose**: Allows users to upload datasets and preview them.
- **Development:** This tab began with just having a user upload file function, I then added a preview data function, 
so the user is able to check which data file they uploaded. Then, I developed a 'use default dataset' function, in case users 
didn't have the correctly formatted dataset - also available to preview. This tab includes try-except errors which
check for correct file format uploaded e.e. csv, xlsx, and also correct column names required.


| ![First Iteration of Upload Tab](images/uploaddata.png) | ![Upload Data Tab](images/upload%20data%202.png) | ![Preview](images/upload%20data%203.png)  |
|---------------------------------------------------------|--------------------------------------------------|-------------------------------------------|
| First Iteration of Upload Tab                           | Final Upload Data Tab                            | Preview of Default Data and Uploaded Data |

- **Features**:
  - Buttons to upload a file or use a default dataset.
  - Dataset preview displayed in a tabular format.

#### Risk Visualisations Tab
- **Purpose**: Provides interactive visualisations for analysing risk scores and liquidity ratios.
- **Development:** The Risk Visualisations Tab provides interactive insights into risk scores and liquidity ratios 
through bar charts and scatter plots. Initially designed as static visualisations, they were iteratively developed 
into interactive tools using Plotly, enabling dynamic data exploration. The inclusion of these visualisations reflects
principles outlined by Munzner (2014), which highlight the importance of interactivity in enhancing data comprehension.
This design choice ensures that users can explore patterns and relationships effectively, supporting better 
decision-making.

| ![First Iteration of Visualisations](images/viz%202.png) | ![First Interactive Visualisations](images/viz%203.png) | ![Risk Visualisations Tab](images/viz%204.png) |
|----------------------------------------------------------|---------------------------------------------------------|------------------------------------------------|
| First Iteration of Visualisations                        | First Interactive Visualisations                        | Final Iteration of Risk Visualisations Tab     |

- **Features**:
  - Bar chart showing risk scores by company.
  - Scatter plot comparing liquidity ratios to risk scores.

---

## Installation Instructions
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps to Install and Run Locally
1. Clone the repository:
   ```bash
   git clone <https://github.com/talia-lyon/Software-Engineering-Summative1-2025.git>
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

## Usage Instructions
1. **Overview Tab**:
   - View high-level metrics such as average risk score and visualise key trends.
2. **Upload Data Tab**:
   - Use the "Choose File" button to upload your dataset.
   - Preview the dataset after uploading to ensure correct format and data integrity.
3. **Risk Visualisations Tab**:
   - Explore bar charts showing risk scores by company and scatter plots comparing liquidity ratios to risk scores.
4. **Help Modal**:
   - Access guidance for each feature by clicking the "Show Help" button in the top-right corner.

![Help Modal](images/help%20modal.png)

---

### Documentation

The project includes detailed documentation to assist both users and developers in understanding and working with the Risk Assessment Dashboard.

#### Available Documentation

1. **[User Documentation](docs/user_documentation.md)**:
   - A comprehensive guide for end-users on how to navigate and use the dashboard's features.
   - Includes detailed instructions for uploading datasets, exploring visualisations, and troubleshooting common issues.

2. **[Technical Documentation](docs/technical_documentation.md)**:
   - A detailed reference for developers and contributors.
   - Covers the project structure, workflows, Flask routes, dependencies, and deployment steps.

#### Location

All documentation files are stored in the `docs/` directory within the project repository:

risk-assessment-dashboard/

├── docs/                    # Documentation (user and technical guides)

│   ├── user_documentation.md   # User instructions for the dashboard

│   ├── technical_documentation.md # Technical details for developers


### How to Access

You can access the documentation directly from this repository:
- [User Documentation](docs/user_documentation.md)
- [Technical Documentation](docs/technical_documentation.md)

---

## Testing and Error Handling
### Testing Approach
The Risk Assessment Dashboard was developed using a Test-Driven Development (TDD) methodology, as outlined by Beck (2022). 
Unit tests validated core functionalities, including file uploads and dataset validation, ensuring robustness. 
Key scenarios, such as handling invalid file types and missing data columns, were addressed. Python’s try-except blocks 
ensured errors were handled gracefully, with clear feedback provided to users. By incorporating TDD, the project not only i
mproved reliability but also adhered to best practices in software quality assurance (Astels, 2003).

Key test scenarios:
- **File Uploads:** Tests validate both successful file uploads and cases of invalid file types or missing files.
- **Dataset Validation:** Ensures that uploaded datasets include all required columns (`Company`, `Industry`, `Risk_Score`, `Liquidity_Ratio`).
- **Data Previews:** Confirms that valid datasets generate accurate HTML previews.

**Error Handling**
The dashboard incorporates Python’s `try-except` blocks to handle errors gracefully and provide users with clear feedback.

- For example, if required columns are missing, the application flashes the message: *"Missing required columns."*
- Unexpected errors prompt a generic message: *"An error occurred while processing the file."*

This approach ensures the application is reliable and user-friendly.

---

## Ethics

As a developer of this Risk Assessment Dashboard, I acknowledge the importance of adhering to ethical principles 
throughout the design, development, and deployment of this application. The following outlines the key ethical 
considerations integrated into this project:

1. **Data Privacy and Security**

- The system ensures that all uploaded data is handled securely, adhering to best practices in data encryption, 
storage, and access controls.
- Users are notified of the purpose and scope of data usage to ensure transparency and compliance with privacy 
laws such as GDPR.
- Uploaded files are validated and sanitised to prevent malicious data injections, ensuring the integrity of the
application.

2. **Bias and Fairness**

- The dashboard aims to provide insights based on objective data. However, it is the responsibility of users to
critically evaluate the source data to avoid perpetuating biases.
- Efforts have been made to design algorithms and processes that treat all data inputs impartially without 
favouritism toward any specific organisation or industry.

3. **Transparency**

- The dashboard provides users with clear error messages and notifications about the success or failure of their 
actions, ensuring they are well-informed throughout the process.
- All calculations, visualisations, and risk metrics are generated in a way that is auditable and reproducible 
to maintain trust in the results.

4. **Accessibility and Usability**

- The application has been designed with user experience in mind, ensuring that it is intuitive and accessible 
for individuals with diverse levels of technical expertise.
- Additional efforts have been made to follow accessibility guidelines (e.g., WCAG) to make the application 
usable by individuals with disabilities.

5. **Accountability**

- While the tool aids in risk assessment, users are reminded that it is not a substitute for professional 
judgement. The tool should be seen as a supplement rather than the sole decision-making mechanism.
- Developers remain committed to maintaining and improving the dashboard to address any emerging ethical 
concerns or user feedback.

---

## Evaluation
### Strengths
- **User-Friendly Interface**: The dashboard provides an intuitive layout, making it easy for users to navigate between tabs and access the required functionality.
- **Flexibility**: Users can upload custom datasets or use the default dataset, ensuring adaptability to various use cases.
- **Interactive Visualisations**: The inclusion of Plotly-based visualisations enhances the analytical capabilities of the tool by allowing dynamic interaction with the data.
- **Help System**: The help modal ensures users can quickly access instructions and guidance, improving overall usability.

### Limitations
- **Data Dependency**: The dashboard relies heavily on the quality and format of the input data. Incorrect or inconsistent data can impact functionality.
- **Scalability**: The current implementation is suitable for small to medium datasets. Performance with large datasets may require optimisation.
- **Limited Visualisation Types**: While the dashboard includes bar charts and scatter plots, additional chart types could provide more comprehensive insights.

### Future Improvements
1. Incorporate advanced filtering options to allow users to drill down into specific data points.
2. Add more visualisation types, such as heatmaps and line charts, to enhance data exploration.
3. Optimise performance for handling large datasets efficiently.
4. Include predictive analytics features to forecast potential risks based on historical data.
5. Implement role-based access control to improve security and customisation for different user groups.

---

## Project Contributions
To contribute to the project:
1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description here"
   ```
4. Push the branch and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```
---

## Contact
For support or suggestions, please contact [Talia Lyon] at [lyon.t@northeastern.edu].

---

### References
1. Beck, K. (2022) *Test-driven development: by example*. Boston: Addison-Wesley.
2. Knaflic, C. N. (2015) *Storytelling with data: a data visualization guide for business professionals*. Hoboken, NJ: Wiley.
3. Munzner, T. (2014) *Visualization analysis and design*. Boca Raton, FL: CRC Press.
4. Royce, W. W. (1987) *Managing the development of large software systems: concepts and techniques*. Proceedings of the 9th International Conference on Software Engineering. Available at: https://doi.org/10.1109/ICSE.1987.10001.
5. Schwaber, K. and Sutherland, J. (2020) *The Scrum guide: the definitive guide to Scrum: the rules of the game*. Available at: https://scrumguides.org/scrum-guide.html (Accessed: 20 January 2025).
6. Sommerville, I. (2016) *Software engineering*. 10th edn. Boston: Pearson.
7. Astels, D. (2003) *Test-driven development: a practical guide*. Boston: Pearson Education.

