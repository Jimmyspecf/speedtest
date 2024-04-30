# SpeedTest Script

A simple yet powerful Python script for measuring download speeds from a server. This script can be particularly useful for network performance monitoring, diagnostics, and ensuring that your internet service provider is delivering the speeds you are paying for. The idea is to make a speedtest script following the example of the service https://speed.limited 
But using Python and uploading/downloading your own file (see the "file_url" string below).

## Description

The SpeedTest Script calculates the download speed by timing how long it takes to download a file from a specified server. This measurement is then converted into Mbps (Megabits per second), providing a clear and concise indication of the network bandwidth.

This tool is designed to be lightweight and easy to use, making it suitable for both beginners and advanced users who need a quick method to assess network speed without the complexity of more extensive testing suites. 

The script can be particularly useful for:
- IT administrators who need to routinely check network performance.
- Software developers who require consistent internet speeds for cloud computing and large data transfers.
- End-users testing their home internet speeds to troubleshoot connectivity issues.
- Researchers conducting fieldwork in various locations where internet speed varies and needs monitoring.

Additionally, the script is versatile and can be adapted or extended to include more functionality, such as simultaneous download and upload speed testing, multi-threaded downloads, and detailed logging for more thorough performance analyses.


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



