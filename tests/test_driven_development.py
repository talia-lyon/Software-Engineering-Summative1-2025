import unittest
import io
from app import create_app


class RiskDashboardTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_file_upload_success(self):
        """Test successful file upload."""
        valid_data = "Company,Industry,Risk_Score,Liquidity_Ratio\nAlpha Corp,Technology,75,1.2\nBeta Ltd,Finance,82," \
                     "0.8\nGamma Inc,Healthcare,65,1.5 "
        data = {"file": (io.BytesIO(valid_data.encode('utf-8')), "valid_file.csv")}
        response = self.client.post('/upload', data=data, content_type='multipart/form-data', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'File uploaded successfully!', response.data)

    def test_invalid_file_type(self):
        """Test uploading an invalid file type."""
        data = {"file": (io.BytesIO(b"This is not a CSV"), "invalid_file.txt")}
        response = self.client.post('/upload', data=data, content_type='multipart/form-data', follow_redirects=True)

        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid file type.', response.data)

    def test_no_file_uploaded(self):
        """Test submitting the form without selecting a file."""
        response = self.client.post('/upload', data={}, content_type='multipart/form-data', follow_redirects=True)

        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No file selected.', response.data)

    def test_missing_required_columns(self):
        """Test uploading a dataset with missing required columns."""
        invalid_data = "Company,Industry\nAlpha Corp,Technology\nBeta Ltd,Finance"
        data = {"file": (io.BytesIO(invalid_data.encode('utf-8')), "missing_columns.csv")}
        response = self.client.post('/upload', data=data, content_type='multipart/form-data', follow_redirects=True)

        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing required columns', response.data)

    def test_preview_valid_file(self):
        """Test previewing a valid file."""
        valid_data = "Company,Industry,Risk_Score,Liquidity_Ratio\nAlpha Corp,Technology,75,1.2\nBeta Ltd,Finance,82," \
                     "0.8\nGamma Inc,Healthcare,65,1.5 "
        data = {"file": (io.BytesIO(valid_data.encode('utf-8')), "valid_file.csv")}
        response = self.client.post('/preview-file', data=data, content_type='multipart/form-data')

        self.assertEqual(response.status_code, 200)
        self.assertIn('dataframe', response.json['preview'])


if __name__ == '__main__':
    unittest.main()
