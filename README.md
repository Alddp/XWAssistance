# XWAssistance

### 使用方法

1. 进入命令行切换工作目录为`main.exe`所在目录

2. 输入`main 命令 参数`

**注意：**使用`format`命令要提前将要格式化的txt名单放到res目录中，并命名为`formated_names.txt`

## 命令列表

|     命令     |   参数    |          功能          |        开发进度         |
|:----------:|:-------:|:--------------------:|:-------------------:|
|   `help`   |    无    |        显示所有命令        |      `Finish`       |
|   `show`   | `文件夹路径` |    显示指定文件夹下的所有文件     |      `Finish`       |
|  `format`  | `文件夹路径` |    匹配姓名后格式化命名(正则)    |      `Finish`       |
| `convert`  | `文件夹路径` |  将中文大写转换为拉伯数字 (正则)   |      `Finish`       |
| `simplify` | `文件夹路径` | 解压文件后两层文件夹名字相同，则删除一层 |      `Finish`       |
|            |         |                      |                     |
|            |         |   一键导出未交名单 (接龙API)   | `under development` |
|            |         |   一键导出文件链接 (接龙API)   | `under development` |
|            |         |                      |                     |
|            |         |         考勤统计         | `under development` |
|            |         |       自动写旷课明细        | `under development` |
|            |         |        课堂回答统计        | `under development` |

### 使用示例

#### `help`命令

输入`main help`，将显示所有可用命令及其简要说明。

#### `show`命令

显示指定文件夹下的所有文件。例如，要显示`/path/to/folder`下的文件，输入：

```bash
main show /path/to/folder
```

#### `format`和`convert`命令

这两个命令用于处理文件名或内容的转换。例如，要对`/path/to/folder`中的文件进行格式化或转换，输入：

```bash
格式化文件名
main format /path/to/folder
转换中文大写为阿拉伯数字
main convert /path/to/folder
```

请确保在使用`format`命令前已将格式化名单（`formated_names.txt`）放置在res目录中。

#### `simplify`命令

该命令用于简化具有相同名称的解压后的文件夹结构。例如：

```bash
main simplify /path/to/folder
```