# flask-server-template
该模板包含构建 Flask 应用程序的最佳实践，处理 API 路由，以及管理数据库交互。

## 开始使用

1. **配置数据库**：
   - 编辑 `configs.py` 文件以设置数据库连接。

2. **定义数据模型**：
   - 在 `models.py` 文件中创建数据模型。

3. **初始化数据库**：
   - 运行 `python init.py` 以自动连接到数据库并创建必要的表。

4. **开发 API**：
   - 在 `app.py` 文件中编写 API 端点。

5. **调试**：
   - 使用 `python app.py` 以调试模式运行应用程序。

6. **生产部署**：
   - 对于生产环境，使用提供的配置模板与 `gunicorn`。
   - 根据需要修改 `gunicorn_cf.py` 文件。
   - 使用 `gunicorn -c gunicorn_cf.py app:app` 运行应用程序。

当然，你也可以使用其他 WSGI 服务器，如 `uWSGI` 或 `waitress` 进行部署。
