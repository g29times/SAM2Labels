# TODO
多文件处理  
训练SAM  
扩展XYWH SAM不规则轮廓选中  
项目编号需要用户输入  
## 已支持
生成的外部文件路径/data/upload  使用单斜线即可  
单图多标签  
id唯一  

# 依赖说明
pip install Pillow（PIL的一个分支） 获取图片的宽度和高度  

# 使用
## label studio
1 下载一张图片  
2 进行SAM解析（postman或gen.py），结果保存为xxx.txt  
3 转换坐标 `python converte.py From.txt To.json width height`  
4 启动 `label-studio start`，创建项目 - 导入图片 - 导入To.json  
生成的结果尚需手动处理：`1 外层括号 2 文件路径 3 在label系统建立对应的新tag 4 导入label`  
* 导入另一台机器的步骤：`1 导出To.json 2 新机器创建项目-打标-导出-获取图片url 3 替换To.json中的文件路径 4 导入`  
## g-sam
`python gen.py`
输入公网url的图片地址，先调用gen，再轮询get
## streamlit
`streamlit run streamlit\streamlit-rounds.py`
Pipeline：上传图片 - 生成url - 调用gen - 调用converte.py


# 安装
## streamlit
`pip install streamlit`
`streamlit hello`
## label studio
https://labelstud.io/guide/install  
1 创建环境 3.10以下 3.8以上 Shift+Ctrl+P - Python create env - 选Venv  
2 激活环境 `& .\.venv\Scripts\activate` - Windows PowerShellx - `set-executionpolicy remotesigned`  
3 安装 `python310 -m pip install label-studio`  
4 启动 `label-studio`  
正确启动日志
 ```
    PS D:\WorkHome\Projects\SELF\ML> label-studio            
    => Database and media directory: C:\Users\Administrator\AppData\Local\label-studio\label-studio
    => Static URL is set to: /static/
    Current platform is win32, apply sqlite fix
    Can't load sqlite3.dll from current directory
    => Database and media directory: C:\Users\Administrator\AppData\Local\label-studio\label-studio
    => Static URL is set to: /static/
    Read environment variables from: C:\Users\Administrator\AppData\Local\label-studio\label-studio\.env
    get 'SECRET_KEY' casted as '<class 'str'>' with default ''
    Starting new HTTPS connection (1): pypi.org:443
    https://pypi.org:443 "GET /pypi/label-studio/json HTTP/1.1" 200 31886
    Performing system checks...

    System check identified no issues (1 silenced).
    May 12, 2024 - 23:36:03
    Django version 3.2.25, using settings 'label_studio.core.settings.label_studio'
    Starting development server at http://0.0.0.0:8080/
    Quit the server with CTRL-BREAK.
    [2024-05-12 23:36:06,440] [django.server::log_message::161] [INFO] "GET / HTTP/1.1" 302 0
```
### 安装注意
1 安装时，使用powershell而不是git bash，安装好venv之后，使用两者进行`python-v`，输出也不同  
### 安装问题
1 PostgreSQL adapter  
`python310 -m pip install psycopg2-binary` https://www.psycopg.org/docs/install.html#build-prerequisites  
2 较高版本的python 如3.12  
ModuleNotFoundError: No module named 'distutils'  
安全：3.10 `python310 -m`  
3 使用312安装时报错  
通常只需要换python版本 无需解决  
error: subprocess-exited-with-error
    Error: pg_config executable not found
    参考：https://blog.csdn.net/wxh0000mm/article/details/96116918