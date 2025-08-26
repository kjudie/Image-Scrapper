# This is a conceptual example, not runnable without API keys.

import requests
import csv
from google.colab import drive
#drive.flush_and_unmount()

# Mount Google Drive
drive.mount('/content/drive')

# Your API credentials
API_KEY = "YOUR_GOOGLE_API_KEY" # Replace with your actual API key or use Colab secrets
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID" # Replace with your actual Search Engine ID

# Define the paths for your files in Google Drive
csv_file_path = '/content/drive/MyDrive/influencers_list.csv' # <<< 1. ALTER THIS LINE >>> Update this path if your file is elsewhere
output_folder_path = '/content/drive/MyDrive/influencer_images' # <<< 2. ALTER THIS LINE >>> Update this path if you want to save images elsewhere

# Make sure the output folder exists
import os
os.makedirs(output_folder_path, exist_ok=True)

# Open the CSV file with influencer names from Google Drive
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        influencer_name = row[0]

        # Build the search query URL
        query = f"{influencer_name} headshot"
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}&searchType=image&num=1"

        # Make the API request
        response = requests.get(url).json()

        # Get the first image URL
        if 'items' in response:
            image_url = response['items'][0]['link']

            # Download and save the image to the specified folder in Google Drive
            image_data = requests.get(image_url).content
            file_name = f"{influencer_name.replace(' ', '_')}.jpg"
            image_save_path = os.path.join(output_folder_path, file_name) # <<< 2. ALTER THIS LINE >>>

            with open(image_save_path, 'wb') as handler:
                handler.write(image_data)
            print(f"Saved image for {influencer_name}")

import requests
import csv
from google.colab import drive
from google.colab import userdata



# Your API credentials
API_KEY = userdata.get("GOOGLE_API_KEY") # Replace with your actual API key or use Colab secrets
SEARCH_ENGINE_ID = userdata.get("SEARCH_ENGINE_ID") # Replace with your actual Search Engine ID




# Define the paths for your files in Google Drive
csv_file_path = '/content/drive/MyDrive/influencers_list.csv' # <<< 1. ALTER THIS LINE >>> Update this path if your file is elsewhere
output_folder_path = '/content/drive/MyDrive/influencer_images' # <<< 2. ALTER THIS LINE >>> Update this path if you want to save images elsewhere

# Make sure the output folder exists
import os
os.makedirs(output_folder_path, exist_ok=True)

# Open the CSV file with influencer names from Google Drive
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        influencer_name = row[0]

        # Build the search query URL
        query = f"{influencer_name} headshot"
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}&searchType=image&num=1"

        # Make the API request
        response = requests.get(url).json()

        # Get the first image URL
        if 'items' in response:
            image_url = response['items'][0]['link']

            # Download and save the image to the specified folder in Google Drive
            image_data = requests.get(image_url).content
            file_name = f"{influencer_name.replace(' ', '_')}.jpg"
            image_save_path = os.path.join(output_folder_path, file_name) # <<< 2. ALTER THIS LINE >>>

            with open(image_save_path, 'wb') as handler:
                handler.write(image_data)
            print(f"Saved image for {influencer_name}")
