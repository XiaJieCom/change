功能：主机管理
实现解析配置文件，执行部分命令


文件架构

stark
    ├── README.txt
    ├── arya
    │   ├── __init__.py
    │   ├── action_list.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── backends							后台处理
    │   │   ├── __init__.py
    │   │   ├── base_module.py					
    │   │   ├── tasks.py
    │   │   └── utils.py
    │   ├── migrations							数据库生成文件
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   ├── models.py
    │   ├── needle
    │   │   ├── conf
    │   │   │   ├── configs.py					配置文件，文件下载，路径配置信息等
    │   │   │   └── registered_modules.py		注册对应的模块
    │   │   ├── core
    │   │   │   ├── main.py
    │   │   │   └── utils.py
    │   │   ├── modules                 		解析配置文件里对应的file、users等
    │   │   │   ├── base_module.py
    │   │   │   ├── files.py					
    │   │   │   └── users.py
    │   │   ├── needle.py						
    │   │   └── var								下载目录	
    │   │       └── downloads
    │   ├── plugins								模块
    │   │   ├── __init__.py
    │   │   ├── cmd.py
    │   │   ├── file.py
    │   │   ├── group.py
    │   │   ├── pkg.py
    │   │   ├── service.py
    │   │   ├── state.py
    │   │   └── user.py
    │   ├── salt.py
    │   ├── salt_configs
    │   │   └── test
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    ├── stark
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── templates


