import json
import requests
import pandas as pd
from io import StringIO

# Load the metadata file
file_path = './metadata.json'  # Path to your JSON metadata file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract site info (latitude, longitude)
site_info = data.get('study', [])[0].get('site', [])[0].get('geo', {}).get('geometry', {}).get('coordinates', [])

# Extract the file URL from the metadata
file_url = data.get('study', [])[0].get('site', [])[0].get('paleoData', [])[0].get('dataFile', [])[0].get('fileUrl', None)

# Extract variable names for the DataFrame headers
variables = data.get('study', [])[0].get('site', [])[0].get('paleoData', [])[0].get('dataFile', [])[0].get('variables', [])

# Extract the variable names as headers
headers = [var.get('cvWhat') for var in variables]


# Download the file from the URL and load it into a DataFrame
if file_url:
    response = requests.get(file_url)
    if response.status_code == 200:
        file_content = response.text
        # Skip comment lines that start with '#'
        data_lines = "\n".join([line for line in file_content.splitlines() if not line.startswith('#')])
        
        # Read the content into a DataFrame and assign custom headers
        df = pd.read_csv(StringIO(data_lines), delimiter='\t', header=0, names=headers)
        
        print("File downloaded and read into DataFrame with custom headers:")
        print(df.head())  # Display the first few rows of the DataFrame
        # Print site info (latitude, longitude)
        if site_info:
            latitude = site_info[0]
            longitude = site_info[1]
            print(f"Latitude: {latitude}, Longitude: {longitude}")
          
            # Save the DataFrame as a CSV file
            output_csv_path = f'./lat_{latitude}_long_{longitude}.csv'
            df.to_csv(output_csv_path, index=False)
            print(f"Data saved to {output_csv_path}")
        else:
            print("Longitude and Latitude not found")
                # Save the DataFrame as a CSV file
            output_csv_path = './output_data.csv'
            df.to_csv(output_csv_path, index=False)
            print(f"Data saved to {output_csv_path}")

        
    else:
        print("Failed to download the file")
else:
    print("No file URL found")



# Optional: Show DataFrame summary
print("\nDataFrame Summary:")
print(df.info())
