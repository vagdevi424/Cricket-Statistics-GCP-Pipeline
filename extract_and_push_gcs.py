import requests
import csv
from google.cloud import storage

# API configuration
api_url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
api_headers = {
    "x-rapidapi-key": "11f5f8f24cmsh2e732aa4f6668f1p10a86cjsn844e8300faa1",  # Replace with your RapidAPI key
    'X-RapidAPI-Host': 'cricbuzz-cricket.p.rapidapi.com'
}
api_params = {
    'formatType': 'odi'
}

# Fetch data from API
response = requests.get(api_url, headers=api_headers, params=api_params)

if response.status_code == 200:
    batsmen_data = response.json().get('rank', [])  # Extracting the 'rank' data
    output_csv_file = 'batsmen_rankings.csv'

    if batsmen_data:
        csv_field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=csv_field_names)
            for batsman in batsmen_data:
                csv_writer.writerow({field: batsman.get(field) for field in csv_field_names})

        print(f"Data fetched successfully and written to '{output_csv_file}'")

        # Upload the CSV file to Google Cloud Storage (GCS)
        gcs_bucket_name = 'bats-ranking-data'
        gcs_client = storage.Client()
        gcs_bucket = gcs_client.bucket(gcs_bucket_name)
        gcs_blob_name = f'{output_csv_file}'  # The path to store in GCS

        gcs_blob = gcs_bucket.blob(gcs_blob_name)
        gcs_blob.upload_from_filename(output_csv_file)

        print(f"File {output_csv_file} uploaded to GCS bucket {gcs_bucket_name} as {gcs_blob_name}")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
