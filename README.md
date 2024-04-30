# SpeedTest Script

A simple script for measuring download speeds from a server.

## Description

This Python script measures the download speed from a specified server by calculating the time taken to download a file and outputs the speed in Mbps.

## Installation

The script requires Python 3.x. First, install the dependencies:

```bash
pip install -r requirements.txt


Usage
Run the script using Python:

python speedtest.py


Configuration
You can change the URL and file size in the script to test different sources and files.

License
This project is distributed under the MIT License.


This file lists the dependencies for the project.


#### `speedtest.py`
```python
import urllib.request
import time

def test_download_speed(download_url, file_size):
    """
    Tests the download speed by downloading a file from the given URL.

    :param download_url: URL of the file to be downloaded.
    :param file_size: Size of the file in bytes.
    """
    start_time = time.time()

    with urllib.request.urlopen(download_url) as response:
        data = response.read()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to download: {elapsed_time} seconds")

    speed_bps = file_size / elapsed_time
    speed_mbps = (speed_bps * 8) / (1024 * 1024)
    
    print(f"Download speed: {speed_mbps:.2f} Mbps")

file_url = 'https://example.com/largefile.zip'
file_size_in_bytes = 100000000  # Replace with the actual file size in bytes
test_download_speed(file_url, file_size_in_bytes)



