# Resume Creator and Downloader
This Flask application allows users to create resumes with custom information and download them as text files. Resumes are stored on Amazon S3 for easy access and sharing.

## Prerequisites
- Python installed on your system
- An Amazon S3 bucket set up for storing resumes
- Flask, Boto3, and python-dotenv Python packages installed

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>

2. Navigate to the project directory:
    ```bash
    cd resume-creator-downloader

3. Install dependencies:
    ```bash
    pip install flask boto3 python-dotenv

## Configuration
1. Create a .env file in the project directory and add the following variables:

    ```plaintext
    AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
    AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
    S3_BUCKET_NAME=<your_s3_bucket_name>
    AWS_REGION=<your_aws_region>
Replace your_aws_access_key_id, your_aws_secret_access_key, your_s3_bucket_name, and your_aws_region with your actual AWS credentials and bucket information.

## Usage
1. Start the Flask server:

    ```bash
    python app.py
    
2. Access the application in your web browser:
    ```arduino
    http://localhost:5000/
    
3. Fill out the resume form with your information and click "Create Resume".

4. After creation, you can download the generated resume by clicking the "Download" link.

## Notes
- Resumes are stored as text files on Amazon S3.
- Each resume file has a unique filename generated with a timestamp.
- Ensure that your S3 bucket has the necessary permissions for uploading and downloading files.

## License
This project is licensed under the MIT License
