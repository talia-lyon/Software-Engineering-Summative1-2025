from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
import os
import pandas as pd
import plotly.express as px
import plotly.io as pio
import io

UPLOAD_FOLDER = 'uploads'
DEFAULT_DATASET = 'app/default_data/financial_risk_dummy_data.csv'  # Path to default dataset
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
VISUALISATIONS_FOLDER = 'app/static/visualisations'

bp = Blueprint('routes', __name__)  # Define a Blueprint

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ensure visualisations folder exists
if not os.path.exists(VISUALISATIONS_FOLDER):
    os.makedirs(VISUALISATIONS_FOLDER)


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_columns(data, required_columns):
    """Validate if the dataset contains all required columns."""
    missing_columns = [col for col in required_columns if col not in data.columns]
    return missing_columns


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        # Render the upload page on GET requests
        return render_template('upload.html')

    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            flash('No file selected.', 'error')
            return render_template('upload.html'), 400

        file = request.files['file']
        if not allowed_file(file.filename):
            flash('Invalid file type.', 'error')
            return render_template('upload.html'), 400

        try:
            # Save the uploaded file
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Validate dataset columns
            if file.filename.endswith('.csv'):
                data = pd.read_csv(filepath)
            elif file.filename.endswith('.xlsx'):
                data = pd.read_excel(filepath)
            else:
                flash('Unsupported file format.', 'error')
                return render_template('upload.html'), 400

            required_columns = {'Company', 'Industry', 'Risk_Score', 'Liquidity_Ratio'}
            if not required_columns.issubset(data.columns):
                flash('Missing required columns.', 'error')
                return render_template('upload.html'), 400

            flash('File uploaded successfully!', 'success')
            return render_template('upload.html'), 200

        except pd.errors.EmptyDataError:
            flash('The uploaded file is empty.', 'error')
            return render_template('upload.html'), 400

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return render_template('upload.html'), 500




@bp.route('/preview-file', methods=['POST'])
def preview_file():
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({'error': 'No file provided.'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only CSV or Excel files are supported.'}), 400

    try:
        if file.filename.endswith('.csv'):
            data = pd.read_csv(file)
        elif file.filename.endswith('.xlsx'):
            data = pd.read_excel(file)
        else:
            return jsonify({'error': 'Unsupported file type.'}), 400

        # Validate required columns
        required_columns = {'Company', 'Industry', 'Risk_Score', 'Liquidity_Ratio'}
        if not required_columns.issubset(set(data.columns)):
            return jsonify({'error': 'Missing required columns'}), 400

        preview_html = data.head(10).to_html(classes='dataframe')
        return jsonify({'preview': preview_html}), 200
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500


@bp.route('/upload-final', methods=['POST'])
def upload_final():
    """Handles the final upload confirmation."""
    try:
        file = request.files.get('file')
        if not file or file.filename == '':
            return jsonify({'message': 'No file provided for upload.'}), 400

        if allowed_file(file.filename):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return jsonify({'message': 'File uploaded successfully!'}), 200
        else:
            return jsonify({'message': 'Invalid file type.'}), 400
    except Exception as e:
        return jsonify({'message': f'Error during upload: {e}'}), 500


@bp.route('/use-default-data', methods=['GET'])
def use_default_data():
    try:
        default_data_path = DEFAULT_DATASET
        data = pd.read_csv(default_data_path)
        preview_html = data.head(10).to_html(classes='dataframe')
        return jsonify({'preview': preview_html}), 200
    except Exception as e:
        return jsonify({'error': f'Error loading default dataset: {str(e)}'}), 500


@bp.route('/visualisations')
def visualisations():
    try:
        # Load the default dataset
        data = pd.read_csv(DEFAULT_DATASET)

        # Check required columns
        required_columns = ['Company', 'Risk_Score', 'Liquidity_Ratio']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Generate interactive bar chart using Plotly
        bar_chart = px.bar(
            data,
            x='Company',
            y='Risk_Score',
            title='Risk Score by Company',
            labels={'Risk_Score': 'Risk Score', 'Company': 'Company'},
        )
        bar_chart.update_layout(title_x=0.5)  # Center align the title
        bar_chart_html = pio.to_html(bar_chart, full_html=False)

        # Generate interactive scatter plot using Plotly
        scatter_plot = px.scatter(
            data,
            x='Risk_Score',
            y='Liquidity_Ratio',
            title='Liquidity Ratio vs Risk Score',
            labels={'Risk_Score': 'Risk Score', 'Liquidity_Ratio': 'Liquidity Ratio'},
        )
        scatter_plot.update_layout(title_x=0.5)  # Center align the title
        scatter_plot_html = pio.to_html(scatter_plot, full_html=False)

        # Render visualisations
        return render_template(
            'visualisations.html',
            bar_chart=bar_chart_html,
            scatter_plot=scatter_plot_html,
        )

    except Exception as e:
        flash(f"Error generating visualisations: {e}")
        return render_template('visualisations.html', error=True)
