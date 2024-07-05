import os
import threading

import requests
from tqdm import tqdm


class DownloadThread(threading.Thread):
    def __init__(self, url, start_byte, end_byte, file_name, progress_callback):
        super().__init__()
        self.url = url
        self.start_byte = start_byte
        self.end_byte = end_byte
        self.file_name = file_name
        self.progress_callback = progress_callback

    def run(self):
        headers = {'Range': f'bytes={self.start_byte}-{self.end_byte}'}
        try:
            r = requests.get(self.url, headers=headers, stream=True)
            with open(self.file_name, 'rb+') as f:
                f.seek(self.start_byte)
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        self.progress_callback(len(chunk))
        except requests.RequestException as e:
            print(f"Error downloading {self.url}: {e}")


def create_empty_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'wb'):
            pass


def multi_threaded_download(urls, num_threads_per_file, file_names):
    threads = []
    file_sizes = []

    def progress_callback(chunk_size):
        progress_bar.update(chunk_size)

    for url, file_name in zip(urls, file_names):
        try:
            r = requests.head(url)
            file_size = int(r.headers.get('Content-Length', 0))
            file_sizes.append(file_size)
            part_size = file_size // num_threads_per_file

            # Ensure file exists before starting threads
            create_empty_file(file_name)

            # Create a tqdm progress bar
            with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_name) as progress_bar:
                for i in range(num_threads_per_file):
                    start_byte = i * part_size
                    end_byte = start_byte + part_size - 1
                    if i == num_threads_per_file - 1:
                        end_byte = file_size - 1

                    thread = DownloadThread(url, start_byte, end_byte, file_name, progress_callback)
                    threads.append(thread)
                    thread.start()

        except requests.RequestException as e:
            print(f"Error with request to {url}: {e}")

    for thread in threads:
        thread.join()

    print("All downloads completed successfully!")


if __name__ == "__main__":
    urls = [
        'https://oss1.qun100.com/ZWE5/V2/formData2/qiKLo7jvIUy98d19b06.zip'
    ]
    num_threads_per_file = 4  # Number of threads per file
    file_names = ['file1.zip']  # File names to save the downloads

    multi_threaded_download(urls, num_threads_per_file, file_names)
