# Overview
 The Job Search POC is a Python-based application that fetches job listings based on user inputs such as job title and location from the Adzuna API. This tool allows users to easily find job opportunities and download the results in a CSV file format. The project is designed as a proof of concept (POC) to demonstrate how to interact with a job search API and process the results.

 # Main Features:

 Search for jobs by title and location.

Fetch job data from Adzuna API.

Save job listings to a CSV file for easy access and analysis.

# Prerequisites

To run this project, you'll need the following:

Python 3.x: Make sure Python is installed on your system.

You can download it from python.org.

pip (Python package installer): pip is needed to install project dependencies.

pip usually comes with Python installations, but if it's not installed, you can follow the instructions from the pip documentation.

Adzuna API Key: You need a valid API key to access job data from the Adzuna API.

To get your API key, you can sign up at the Adzuna Developer Portal.

Setup Instructions

1. Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/Swetha302/job_search_poc.git

2. Set Up a Virtual Environment (Optional)
It’s recommended to use a virtual environment. To set it up:

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

3. Install Dependencies
Install the required Python libraries:
pip install -r requirements.txt

4. Set Up Your Adzuna API Key
In the search_jobs.py file, replace the placeholder YOUR_API_KEY with your actual Adzuna API key:

API_KEY = "YOUR_API_KEY"

How to Use
1. Run the Script
Run the script with a job title and location as inputs:

python search_jobs.py --title "Data Engineer" --location "New York"
This will search for jobs titled Data Engineer in New York.

2. Check the Output
The script will create a jobs.csv file with the following details for each job:

Job Title

Company

Location

Job Description

Salary

Date Posted

Job URL
