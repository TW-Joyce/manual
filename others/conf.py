# conf.py

# 项目信息
project = "My Project"
copyright = "2025, Your Name"
author = "Your Name"

# 版本信息
version = "1.0"
release = "1.0.0"

# 扩展插件
extensions = [
    "sphinx.ext.autodoc",  # 自动生成代码文档
    "sphinx.ext.napoleon",  # 支持 NumPy 和 Google 风格的注释
    "myst_parser"  # 支持 Markdown
]

# 主题设置
html_theme = "sphinx_rtd_theme"  # 使用 Read the Docs 主题
html_static_path = ["_static"]