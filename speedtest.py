
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
