import json


class FileError:
    @staticmethod
    def output(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except FileNotFoundError as e:
                print(f"{func.__name__}无法找到命令文件: ", e)
            except json.JSONDecodeError as e:
                print(f"{func.__name__}无法解析json文件的内容", e)
            except ValueError as e:

                print(func.__name__, e)
            except Exception as e:
                print(func.__name__, e)

        return wrapper
