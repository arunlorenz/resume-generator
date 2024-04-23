import os
import boto3
import time
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file

# Flask application setup
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# AWS credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_REGION = os.getenv('AWS_REGION')

# S3 client initialization
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


@app.route('/')
def resume_form():
    return render_template('resume_form.html')


@app.route('/create_resume', methods=['POST'])
def create_resume():
    name = request.form['name']
    roll_no = request.form['roll_no']
    degree = request.form['degree']
    HSC = request.form['HSC']
    experience = request.form['experience']
    skills = request.form['skills']
    linkedin = request.form['linkedin']
    github = request.form['github']
    mobile = request.form['mobile']
    email = request.form['email']

    # Create resume content
    resume_content = f"""
{name}
{roll_no}
Degree in : {degree}

Github : {github}
LinkedIn : {linkedin}

HSC: {HSC}

Experience:
{experience}

Skills:
{skills}

Contact:
{mobile}
{email}
"""

    # Generate unique filename with timestamp
    filename = f"{name}_{int(time.time())}.txt"

    # Save resume content to local file (optional, for testing or debugging)
    with open(filename, 'w') as f:
        f.write(resume_content)

    # Upload resume to S3 bucket
    try:
        s3_client.upload_file(filename, S3_BUCKET_NAME, filename)
        os.remove(filename)  # Remove local file after upload (optional)
        message = "Resume created and uploaded successfully!"
    except Exception as e:
        message = f"An error occurred: {str(e)}"

    return render_template('resume_created.html', message=message, filename=filename)


from flask import Response

@app.route('/download_resume/<filename>')
def download_resume(filename):
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=filename)
        try:
            attachment_filename = filename
            content = response['Body'].read()
            return Response(
                content,
                mimetype='text/plain',
                headers={
                    'Content-Disposition': f'attachment; filename="{attachment_filename}"'
                }
            )
        except KeyError:
            # Handle case where filename is not found in the response
            message = "Filename not found in response."
            return render_template('resume_created.html', message=message)
    except Exception as e:
        message = f"An error occurred: {str(e)}"
        return render_template('resume_created.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
