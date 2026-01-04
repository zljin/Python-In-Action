# Python-In-Action

https://www.cnblogs.com/derek1184405959/p/8579428.html

https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-zh.md#python


# 虚拟开发环境

**工具链迁移**
   - Maven/Gradle → `pip` + `requirements.txt`
   - JUnit → `pytest`
   - IDEA → PyCharm/VSCode配置

> vitualenv 保证每个python项目 依赖版本的独立性

```sh
# 1. install virtualenv tool by pip
pip install virtualenv

# 2. create virtualenv and directory name is venv
virtualenv venv

# 3. switch virtual env
## windows
venv\Scripts\activate
## macbook
source venv/bin/activate 

# 4. view all Dependencies
pip list

# 5. like maven install some Dependencies
pip install -r requirements.txt

# 6. download current Dependencies and version in requirements.txt (optional)
pip freeze > requirements.txt

# 7. logout virtual env
deactive
```

> cmd setup 虚拟环境的Python sdk

```sh
virual_python_bin_path="d:/Codes/venv/Scripts"
python_code_dir="d:/Codes/basics"

${virual_python_bin_path}/python.exe ${python_code_dir}/1.py
```


> vscode setup 虚拟环境的Python sdk

打开命令面板：

Windows/Linux: Ctrl + Shift + P

macOS: Cmd + Shift + P

输入并选择Python: Select Interpreter

在弹出的列表中，找到你的虚拟环境路径(例如:myenv/bin/python 或 myenv\Scripts\python.exe)

选择虚拟环境的Python解释器。
