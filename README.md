# Clucker

Clucker 是一个使用 Django 构建的轻量级微博应用。用户可以创建账户、发布短消息（Cluck）、关注其他用户，并在个人动态中查看自己与所关注用户的最新内容。

## 功能特性

- 用户注册、登录与退出
- 编辑个人资料和修改密码
- 发布最多 280 个字符的短消息
- 浏览用户列表和用户主页
- 关注或取消关注其他用户
- 在动态流中查看自己及所关注用户的消息
- 使用 Gravatar 显示用户头像
- Django Admin 后台管理
- 完整的模型、表单和视图自动化测试

## 技术栈

- Python 3.8+
- Django 3.2.5
- SQLite
- Bootstrap 5
- django-widget-tweaks
- Faker

## 快速开始

### 1. 创建并激活虚拟环境

macOS / Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell：

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. 安装依赖

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. 初始化数据库

```bash
python manage.py migrate
```

项目默认使用根目录下的 `db.sqlite3` SQLite 数据库。

### 4. 启动开发服务器

```bash
python manage.py runserver
```

浏览器访问：<http://127.0.0.1:8000/>

## 示例数据

项目提供了用于生成和清理测试用户的管理命令。

生成 100 个随机用户：

```bash
python manage.py seed
```

这些随机用户的统一密码为 `Password123`。用户名和邮箱由 Faker 随机生成。

删除所有非管理员用户及其关联内容：

```bash
python manage.py unseed
```

> `unseed` 会直接删除数据，执行前请确认当前数据库中没有需要保留的普通用户。

## 创建管理员账户

```bash
python manage.py createsuperuser
```

创建完成后，可访问 <http://127.0.0.1:8000/admin/> 登录 Django Admin。

## 运行测试

```bash
python manage.py test
```

生成测试覆盖率报告：

```bash
coverage run manage.py test
coverage report
```

如需生成 HTML 报告：

```bash
coverage html
```

随后打开 `htmlcov/index.html` 查看结果。

## 账户规则

- 用户名必须以 `@` 开头，后面至少包含 3 个字母、数字或下划线字符。
- 密码必须同时包含大写字母、小写字母和数字。
- 用户简介最多 520 个字符。
- 每条消息最多 280 个字符。

## 项目结构

```text
.
├── clucker/                   # Django 项目配置、URL、ASGI 和 WSGI 入口
├── microblogs/                # 微博应用
│   ├── management/commands/   # seed 和 unseed 管理命令
│   ├── migrations/            # 数据库迁移
│   ├── templates/             # 页面模板
│   ├── tests/                 # 自动化测试
│   ├── forms.py               # 登录、注册、资料、密码和发帖表单
│   ├── models.py              # User 和 Post 数据模型
│   └── views.py               # 页面与业务逻辑
├── static/                    # 样式、字体和图片资源
├── manage.py                  # Django 命令行入口
└── requirements.txt           # Python 依赖
```

## 主要路由

| 路径 | 说明 |
| --- | --- |
| `/` | 首页 |
| `/sign_up/` | 注册 |
| `/log_in/` | 登录 |
| `/feed/` | 个人动态流 |
| `/users/` | 用户列表 |
| `/profile/` | 编辑个人资料 |
| `/password/` | 修改密码 |
| `/admin/` | Django Admin |

## 开发说明

当前 `clucker/settings.py` 中启用了 `DEBUG`，并包含开发用的 `SECRET_KEY`。这些设置只适用于本地开发；部署到生产环境前，请通过环境变量管理密钥、关闭调试模式、配置 `ALLOWED_HOSTS`，并执行 Django 的部署检查：

```bash
python manage.py check --deploy
```

页面通过 CDN 加载 Bootstrap 及 Bootstrap Icons，因此首次加载页面时需要可访问互联网。
