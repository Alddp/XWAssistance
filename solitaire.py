import requests


class Solitaire:
    head_url = "https://form.qun100.com"

    def __init__(self, app_id: str, secret: str, form_id: str, access_token: str | None = None):
        self.app_id = app_id
        self.secret = secret
        self.form_id = form_id
        self.access_token = access_token

        self.nicknames = []  # 昵称
        self.names = []  # 姓名
        self.urls = []  # 文件地址
        self.filenames = []  # 文件名

    def update_token(self):
        """更新token"""
        body_url = f"/openapi/v1/refreshAccessToken?appId={self.app_id}&secret={self.secret}"
        url = self.head_url + body_url
        response = requests.get(url).json()
        self.access_token = response["data"]["accessToken"]
        return self.access_token

    def get_datas(self) -> dict:
        """获取json格式数据"""
        body_url = f"/openapi/v1/form/data?accessToken={self.access_token}"
        url = self.head_url + body_url

        headers = {"Content-Type": "application/json"}
        data = {"formId": self.form_id}

        response = requests.post(url, json=data, headers=headers).json()
        return response

    def parse_data(self, data_json: dict):
        """解析json数据"""
        for item in data_json["data"]["list"]:
            self.nicknames.append(item["nickname"])
            self.names.append(item["catalogs"][0]["value"])
            self.urls.append(item["catalogs"][1]["value"][0]["url"])
            self.filenames.append(item["catalogs"][1]["value"][0]["fileName"])

    def download_file(self, save_path):

        for name, url in zip(self.names, self.urls):
            try:
                # 发起GET请求并获取响应对象
                response = requests.get(url)
                # 检查响应状态码
                if response.status_code == 200:
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                    print(f"文件已保存到 {save_path}")
                else:
                    print(f"下载失败：HTTP 状态码 {response.status_code}")
            except Exception as e:
                print(f"下载失败：{e}")


if __name__ == '__main__':
    app_id = "6etSQFFI"
    secret = "JVcQNpBoZ9VYWOwzDOM9NS8HxsPTNTx2"
    form_id = "1596670615441285120"

    jl = Solitaire(app_id, secret, form_id)

    jl.update_token()
    datas = jl.get_datas()
    jl.parse_data(datas)
    print(jl.urls)
