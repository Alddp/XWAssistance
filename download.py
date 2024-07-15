import os
import threading

import requests


class MultiThreadedDownloader:
    """
    多线程下载器类，用于从给定URL下载文件到指定路径。

    参数:
    url: 文件的URL。
    output_path: 文件下载后的保存路径。
    num_threads: 下载时使用的线程数量，默认为5。

    属性:
    url: 文件的URL。
    output_path: 文件的保存路径。
    num_threads: 下载使用的线程数量。
    total_size: 文件的总大小。
    ranges: 文件划分的下载范围列表。
    """

    def __init__(self, url, output_path, num_threads=5):
        self.url = url
        self.output_path = output_path
        self.num_threads = num_threads
        self.total_size = 0
        self.ranges = []

    def _get_file_size(self):
        """
        获取文件的总大小。
        """
        response = requests.head(self.url)
        self.total_size = int(response.headers.get('content-length', 0))

    def _split_file(self):
        """
        根据文件大小和线程数量划分文件下载范围。
        """
        chunk_size = self.total_size // self.num_threads
        self.ranges = [(i * chunk_size, (i + 1) * chunk_size - 1) for i in range(self.num_threads)]
        self.ranges[-1] = (self.ranges[-1][0], self.total_size - 1)

    def _download_thread(self, i, start, end):
        """
        每个线程执行的下载任务。

        参数:
        i: 线程编号。
        start: 下载范围的起始字节。
        end: 下载范围的结束字节。
        """
        headers = {'Range': f'bytes={start}-{end}'}
        response = requests.get(self.url, headers=headers, stream=True)

        with open(f'{self.output_path}.part{i}', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    def download(self):
        """
        启动多线程下载文件。
        """
        self._get_file_size()
        self._split_file()

        threads = []
        for i, (start, end) in enumerate(self.ranges):
            thread = threading.Thread(target=self._download_thread, args=(i, start, end))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        with open(self.output_path, 'wb') as outfile:
            for i in range(self.num_threads):
                with open(f'{self.output_path}.part{i}', 'rb') as infile:
                    outfile.write(infile.read())
                os.remove(f'{self.output_path}.part{i}')  # 删除临时文件
