import csv
import requests
import json

API_ID = "53309e4f"
API_KEY = "362bda54c64f4329c05d2918ea22adbd"
BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"

def fetch_jobs(title, location):
    params = {
        "app_id": API_ID.strip(),
        "app_key": API_KEY.strip(),
        "what": title,
        "where": location,
        "max_days_old": 1  # Get only recent jobs
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        jobs = response.json().get("results", [])
        return jobs
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return []

def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Location", "Company", "Salary Min", "Salary Max", "Job Link"])
        
        for job in jobs:
            writer.writerow([
                job.get("title", "N/A"),
                job.get("location", {}).get("display_name", "N/A"),
                job.get("company", {}).get("display_name", "N/A"),
                job.get("salary_min", "N/A"),
                job.get("salary_max", "N/A"),
                job.get("redirect_url", "N/A")
            ])
    
    print(f"✅ Jobs saved to `{filename}`")

# Run script
if __name__ == "__main__":
    title = input("Enter job title: ")
    location = input("Enter job location: ")

    jobs = fetch_jobs(title, location)

    if jobs:
        print(f"\n✅ Found {len(jobs)} jobs! Saving to CSV...\n")
        save_to_csv(jobs)
    else:
        print("❌ No jobs found.")


