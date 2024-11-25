import requests
import csv

# API endpoint for cricket rankings
api_url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

# Query parameters for fetching Test rankings
query_parameters = {"formatType": "test"}

# API headers with authentication details
api_headers = {
    "x-rapidapi-key": "11f5f8f24cmsh2e732aa4f6668f1p10a86cjsn844e8300faa1",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

# Adjusted query parameters for ODI format
query_format = {'formatType': 'odi'}

# Sending GET request to the API
response = requests.get(api_url, headers=api_headers, params=query_format)

# Check if the response is successful
if response.status_code == 200:
    # Extract 'rank' data from the response
    rankings_data = response.json().get('rank', [])
    output_csv_file = 'batsmen_rankings.csv'

    # If data is available, process and write to CSV
    if rankings_data:
        column_headers = ['rank', 'name', 'country']  # Specify the required column headers

        # Write the data to a CSV file
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=column_headers)
            # csv_writer.writeheader()  # Uncomment if headers are needed
            for player in rankings_data:
                csv_writer.writerow({header: player.get(header) for header in column_headers})

        print(f"Data fetched successfully and written to '{output_csv_file}'")
    else:
        print("No data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)
