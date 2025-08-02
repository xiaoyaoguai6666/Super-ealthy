# PythonAnywhere 部署指南

## 快速部署步骤

### 1. 准备文件

确保您有以下文件结构：
```
健康管理系统/
├── app.py
├── requirements.txt
├── README.md
├── DEPLOYMENT.md
├── test_app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── upload.html
├── static/
│   ├── css/
│   └── js/
└── uploads/
```

### 2. 上传到PythonAnywhere

1. 登录您的PythonAnywhere账户
2. 进入"Files"选项卡
3. 在`/home/yourusername/`目录下创建新文件夹（例如：`health_app`）
4. 上传所有文件到该文件夹

### 3. 安装依赖

1. 进入"Consoles"选项卡
2. 打开一个新的Bash控制台
3. 运行以下命令：

```bash
cd /home/yourusername/health_app
pip install --user -r requirements.txt
```

### 4. 创建Web应用

1. 进入"Web"选项卡
2. 点击"Add a new web app"
3. 选择"Manual configuration"
4. 选择Python版本（推荐3.9或更高）
5. 在"Code"部分设置：
   - Source code: `/home/yourusername/health_app`
   - Working directory: `/home/yourusername/health_app`

### 5. 配置WSGI文件

1. 点击WSGI configuration file链接
2. 找到并编辑WSGI文件
3. 将内容替换为：

```python
import sys
import os

# 添加项目路径
path = '/home/yourusername/health_app'
if path not in sys.path:
    sys.path.append(path)

# 设置环境变量
os.environ['FLASK_ENV'] = 'production'

# 导入应用
from app import app as application

# 可选：设置应用配置
application.config['SECRET_KEY'] = 'your-production-secret-key'
```

### 6. 创建数据库

1. 进入"Consoles"选项卡
2. 打开一个新的Python控制台
3. 运行以下命令：

```python
import sys
sys.path.append('/home/yourusername/health_app')
from app import app, db

with app.app_context():
    db.create_all()
    print("数据库表创建成功！")
```

### 7. 设置静态文件

1. 回到"Web"选项卡
2. 在"Static files"部分添加：
   - URL: `/static/`
   - Directory: `/home/yourusername/health_app/static/`

### 8. 重启应用

1. 点击"Reload"按钮
2. 等待几秒钟让应用重启
3. 访问您的网站URL

## 故障排除

### 常见问题

#### 1. 模块导入错误
**错误**: `ModuleNotFoundError: No module named 'flask'`
**解决方案**: 
```bash
pip install --user flask flask-sqlalchemy werkzeug
```

#### 2. 数据库错误
**错误**: `sqlite3.OperationalError: no such table`
**解决方案**: 重新创建数据库表
```python
from app import app, db
with app.app_context():
    db.drop_all()
    db.create_all()
```

#### 3. 权限错误
**错误**: `PermissionError: [Errno 13] Permission denied`
**解决方案**: 确保uploads文件夹存在且有写入权限
```bash
mkdir -p uploads
chmod 755 uploads
```

#### 4. 静态文件不加载
**解决方案**: 检查静态文件配置是否正确

### 调试技巧

1. **查看错误日志**：
   - 在"Web"选项卡中点击"Error log"查看详细错误信息

2. **测试应用**：
   ```bash
   cd /home/yourusername/health_app
   python3 test_app.py
   ```

3. **检查文件权限**：
   ```bash
   ls -la /home/yourusername/health_app
   ```

## 安全配置

### 1. 更改密钥
在`app.py`中更改SECRET_KEY：
```python
app.config['SECRET_KEY'] = 'your-very-secure-secret-key-here'
```

### 2. 设置环境变量
在WSGI文件中添加：
```python
import os
os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = 'your-secret-key'
```

### 3. 限制文件上传
在`app.py`中设置：
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

## 维护指南

### 1. 备份数据库
```bash
cp /home/yourusername/health_app/health_app.db /home/yourusername/backup/
```

### 2. 清理上传文件
定期清理不需要的文件以节省空间

### 3. 监控日志
定期检查错误日志以发现潜在问题

### 4. 更新应用
1. 上传新版本文件
2. 重启Web应用
3. 测试功能是否正常

## 性能优化

### 1. 启用压缩
在WSGI文件中添加：
```python
from werkzeug.middleware.proxy_fix import ProxyFix
application = ProxyFix(application, x_for=1, x_proto=1, x_host=1, x_prefix=1)
```

### 2. 缓存静态文件
在Web应用配置中设置缓存头

### 3. 数据库优化
定期清理和优化SQLite数据库

## 联系支持

如果遇到问题，请：
1. 检查错误日志
2. 运行测试脚本
3. 查看PythonAnywhere文档
4. 联系PythonAnywhere支持

---

**注意**: 请将上述代码中的`yourusername`和`health_app`替换为您的实际用户名和项目文件夹名。 