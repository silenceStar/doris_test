my_project/                   # 项目根目录
│── my_project/               # 主要应用代码
│   ├── __init__.py
│   ├── main.py
│   ├── config.py             # 项目配置
│   ├── utils.py
│   ├── models/               # 数据模型（ORM / 业务逻辑）
│   │   ├── __init__.py
│   │   ├── user_model.py
│── tests/                    # 测试代码
│── sql/                      # SQL 相关文件（DDL、DML）
│   ├── schema.sql            # DDL：数据库表结构
│   ├── init_data.sql         # DML：初始数据
│   ├── migrations/           # 数据库迁移脚本（如 Alembic）
│       ├── 001_init.up.sql
│       ├── 002_add_index.up.sql
│── docker/                   # Docker 相关配置
│   ├── Dockerfile            # 构建 Docker 镜像
│   ├── docker-compose.yaml   # 管理多个容器
│   ├── .dockerignore         # 忽略不必要的文件
│── configs/                  # 额外的配置（YAML、ENV）
│   ├── app.yaml              # 应用配置
│   ├── db.yaml               # 数据库配置
│── docs/                     # 文档
│   ├── README.md
│── requirements.txt          # 依赖列表
│── setup.py                  # Python 包安装
│── .gitignore                # Git 忽略文件
│── LICENSE                   # 许可证
