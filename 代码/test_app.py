#!/usr/bin/env python3
"""
健康管理系统测试脚本
用于验证应用的基本功能
"""

import os
import sys
from app import app, db, User, HealthFile

def test_database():
    """测试数据库连接和表创建"""
    print("🔍 测试数据库连接...")
    try:
        with app.app_context():
            # 检查表是否存在
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"✅ 数据库连接成功，发现 {len(tables)} 个表")
            return True
    except Exception as e:
        print(f"❌ 数据库连接失败: {e}")
        return False

def test_routes():
    """测试路由是否正常"""
    print("🔍 测试路由...")
    routes = [
        '/',
        '/register',
        '/login',
        '/dashboard',
        '/upload'
    ]
    
    with app.test_client() as client:
        for route in routes:
            try:
                response = client.get(route)
                if response.status_code in [200, 302]:  # 200 OK 或 302 重定向
                    print(f"✅ 路由 {route} 正常")
                else:
                    print(f"⚠️  路由 {route} 返回状态码 {response.status_code}")
            except Exception as e:
                print(f"❌ 路由 {route} 测试失败: {e}")

def test_file_structure():
    """测试文件结构"""
    print("🔍 检查文件结构...")
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md'
    ]
    
    required_dirs = [
        'templates',
        'static',
        'uploads'
    ]
    
    required_templates = [
        'templates/base.html',
        'templates/index.html',
        'templates/register.html',
        'templates/login.html',
        'templates/dashboard.html',
        'templates/upload.html'
    ]
    
    # 检查必需文件
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ 文件 {file} 存在")
        else:
            print(f"❌ 文件 {file} 缺失")
    
    # 检查必需目录
    for dir in required_dirs:
        if os.path.exists(dir):
            print(f"✅ 目录 {dir} 存在")
        else:
            print(f"❌ 目录 {dir} 缺失")
    
    # 检查模板文件
    for template in required_templates:
        if os.path.exists(template):
            print(f"✅ 模板 {template} 存在")
        else:
            print(f"❌ 模板 {template} 缺失")

def main():
    """主测试函数"""
    print("🚀 开始健康管理系统测试...")
    print("=" * 50)
    
    # 测试文件结构
    test_file_structure()
    print()
    
    # 测试数据库
    test_database()
    print()
    
    # 测试路由
    test_routes()
    print()
    
    print("=" * 50)
    print("✅ 测试完成！")
    print("\n📝 部署说明:")
    print("1. 确保所有文件都已上传到PythonAnywhere")
    print("2. 安装依赖: pip install -r requirements.txt")
    print("3. 配置WSGI文件")
    print("4. 创建数据库: python -c 'from app import app, db; app.app_context().push(); db.create_all()'")
    print("5. 重启Web应用")

if __name__ == '__main__':
    main() 