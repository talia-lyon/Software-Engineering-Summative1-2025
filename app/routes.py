from flask import Blueprint, request, jsonify, render_template
import os

bp = Blueprint("routes", __name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"csv"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file types
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# In-memory storage for uploaded file details (replace with JSON or database later)
uploaded_files = []

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # Save file details in memory
        uploaded_files.append({"filename": file.filename, "path": filepath})
        return jsonify({"success": "File uploaded successfully!"}), 200
    return jsonify({"error": "Invalid file type"}), 400

@bp.route("/data", methods=["GET"])
def get_data():
    return jsonify(uploaded_files)
