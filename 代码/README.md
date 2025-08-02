# 健康管理系统

一个基于Flask的现代化健康数据管理Web应用程序，专为PythonAnywhere平台设计。

## 功能特性

- 🔐 **用户认证系统** - 安全的注册和登录功能
- 📁 **文件管理** - 上传、下载、删除健康相关文件
- 🎨 **现代化UI** - 响应式设计，美观的用户界面
- 🔒 **数据安全** - 文件加密存储，用户权限控制
- 📊 **数据统计** - 文件类型统计和用户数据概览

## 支持的文件类型

- PDF文档 (.pdf)
- Word文档 (.doc, .docx)
- 图片文件 (.jpg, .jpeg, .png, .gif)
- Excel表格 (.xls, .xlsx)
- CSV数据文件 (.csv)
- 其他健康相关文件

## 本地开发

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
python app.py
```

应用将在 `http://localhost:5000` 启动

## PythonAnywhere 部署

### 1. 上传文件

将以下文件上传到您的PythonAnywhere账户：

- `app.py`
- `requirements.txt`
- `templates/` 文件夹
- `static/` 文件夹

### 2. 安装依赖

在PythonAnywhere的Bash控制台中运行：

```bash
pip install --user -r requirements.txt
```

### 3. 配置Web应用

1. 进入PythonAnywhere的Web选项卡
2. 点击"Add a new web app"
3. 选择"Manual configuration"
4. 选择Python版本（推荐3.9或更高）
5. 在"Code"部分设置：
   - Source code: `/home/yourusername/yourproject`
   - Working directory: `/home/yourusername/yourproject`
   - WSGI configuration file: 编辑并添加以下代码

### 4. 配置WSGI文件

在WSGI配置文件中添加：

```python
import sys
path = '/home/yourusername/yourproject'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### 5. 创建数据库

在PythonAnywhere的Python控制台中运行：

```python
from app import app, db
with app.app_context():
    db.create_all()
```

### 6. 设置静态文件

在Web应用配置中设置静态文件映射：
- URL: `/static/`
- Directory: `/home/yourusername/yourproject/static/`

### 7. 重启应用

点击"Reload"按钮重启Web应用。

## 使用说明

### 注册新用户

1. 访问网站主页
2. 点击"注册"按钮
3. 填写用户名、邮箱和密码
4. 提交注册表单

### 登录系统

1. 点击"登录"按钮
2. 输入用户名和密码
3. 点击登录

### 上传文件

1. 登录后进入个人主页
2. 点击"上传文件"按钮
3. 选择要上传的文件
4. 添加可选的描述信息
5. 点击"上传文件"

### 管理文件

- **下载文件**: 点击文件卡片中的"下载"按钮
- **删除文件**: 点击文件卡片中的"删除"按钮
- **查看统计**: 在个人主页查看文件统计信息

## 安全特性

- 密码加密存储
- 文件访问权限控制
- 安全的文件上传验证
- 用户会话管理

## 技术栈

- **后端**: Flask, SQLAlchemy
- **前端**: Bootstrap 5, Font Awesome
- **数据库**: SQLite
- **部署**: PythonAnywhere

## 文件结构

```
健康管理系统/
├── app.py                 # 主应用文件
├── requirements.txt       # Python依赖
├── README.md             # 项目说明
├── templates/            # HTML模板
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── upload.html
├── static/              # 静态文件
│   ├── css/
│   └── js/
└── uploads/             # 上传文件存储
```

## 注意事项

1. 确保上传文件夹有适当的写入权限
2. 定期备份数据库文件
3. 监控磁盘空间使用情况
4. 定期清理不需要的文件

## 许可证

MIT License 