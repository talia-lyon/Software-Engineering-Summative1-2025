from flask import Blueprint, render_template, request, jsonify, flash
import os
import pandas as pd

UPLOAD_FOLDER = 'uploads'
DEFAULT_DATASET = 'app/default_data/financial_risk_dummy_data.csv'  # Path to default dataset
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

bp = Blueprint('routes', __name__)  # Define a Blueprint

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Root route
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            flash('Upload successful!')
            return render_template('upload.html', preview_file=file.filename)
        else:
            flash('Invalid file type. Please upload a CSV or Excel file.')
            return redirect(request.url)
    return render_template('upload.html')

@bp.route('/preview-file', methods=['POST'])
def preview_file():
    """Handles the AJAX request for previewing uploaded data."""
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({'error': 'No file provided.'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only CSV or Excel files are supported.'}), 400

    try:
        # Read and process the uploaded file
        if file.filename.endswith('.csv'):
            data = pd.read_csv(file)
        elif file.filename.endswith('.xlsx'):
            data = pd.read_excel(file)
        else:
            return jsonify({'error': 'Unsupported file type.'}), 400

        # Convert the first 10 rows to HTML
        preview_html = data.head(10).to_html(classes='dataframe')
        return jsonify({'preview': preview_html}), 200
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500


@bp.route('/upload-final', methods=['POST'])
def upload_final():
    """Handles the final upload confirmation."""
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({'message': 'No file provided for upload.'}), 400

    if allowed_file(file.filename):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return jsonify({'message': 'Upload successful!'}), 200
    else:
        return jsonify({'message': 'Invalid file type. Please upload a CSV or Excel file.'}), 400

@bp.route('/use-default-data', methods=['GET'])
def use_default_data():
    """Handles the AJAX request to preview the default dataset."""
    try:
        data = pd.read_csv(DEFAULT_DATASET)
        # Convert the first 10 rows to HTML
        preview_html = data.head(10).to_html(classes='dataframe')
        return jsonify({'preview': preview_html}), 200
    except Exception as e:
        return jsonify({'error': f"Error loading default dataset: {str(e)}"}), 500
