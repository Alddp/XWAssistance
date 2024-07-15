import json

import requests

from download import MultiThreadedDownloader


class Solitaire:
    head_url = "https://form.qun100.com"

    def __init__(self, form_id):
        self.app_id = ""
        self.secret = ""
        self.form_id = form_id
        self.access_token = ""

        self.nicknames = []  # 昵称
        self.names = []  # 姓名
        self.urls = []  # 文件地址
        self.filenames = []  # 文件名

    def __init_info(self):
        """初始化信息"""
        with open("data/solitaire.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.app_id = data["app_id"]
            self.secret = data["secret"]

    def __check_info(self):
        """检查信息是否初始化完成"""
        if self.app_id == "" or self.secret == "":
            print("请先在data/solitaire.json中填写app_id和secret")
            exit()

    def __update_token(self):
        """更新token"""
        body_url = f"/openapi/v1/refreshAccessToken?appId={self.app_id}&secret={self.secret}"
        url = self.head_url + body_url
        response = requests.get(url).json()
        try:
            self.access_token = response["data"]["accessToken"]
        except Exception as e:
            print(response)
            print(e)
        return self.access_token

    def get_datas(self) -> dict:
        self.__init_info()  # 初始化信息
        self.__check_info()  # 检查信息是否初始化完成
        self.__update_token()

        """获取json格式数据"""
        body_url = f"/openapi/v1/form/data?accessToken={self.access_token}"
        url = self.head_url + body_url

        headers = {"Content-Type": "application/json"}
        data = {"formId": self.form_id}

        response = requests.post(url, json=data, headers=headers).json()

        self.__parse_data(response)
        return response

    def export_files(self, save_path):
        """导出文件"""
        self.get_datas()

        for url, filename, name in zip(self.urls, self.filenames, self.names):
            print(f"{name}下载中.......")
            downloader = MultiThreadedDownloader(url=url, output_path=f"{save_path}/{filename}", num_threads=10)
            downloader.download()
        print("导出完成")

    def __parse_data(self, data_json: dict):
        """解析json数据"""
        for item in data_json["data"]["list"]:
            self.nicknames.append(item["nickname"])
            self.names.append(item["catalogs"][0]["value"])
            self.urls.append(item["catalogs"][1]["value"][0]["url"])
            self.filenames.append(item["catalogs"][1]["value"][0]["fileName"])
