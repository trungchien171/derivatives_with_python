import requests

# URL of the file
url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt"

# Download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a local file
    with open("hbrbcpe.txt", "wb") as file:
        file.write(response.content)
    print("File downloaded and saved as 'hbrbcpe.txt'")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
