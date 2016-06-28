blog：http://www.cnblogs.com/xiajie/p/5488431.html


主要项目为 CRM,其他部分可忽略


1 基本登录
2 校区/用户/讲师/课程/咨询记录 等信息的编辑


访问说明:


http://127.0.0.1:8000/crm         默认用户名和密码    tom:1234qwer 或者 admin:1234qwer

登录后左侧为导航栏,默认显示crm下的菜单,右上角为当前登录用户
点击对应标签显示为对应信息

以课程简介为例,实现了增加/全选/反选/取消/删除/编辑等功能
部分目录功能没有完全实现,课程简介较全

目录结构
├── admin.py
├── apps.py
├── forms.py                modelform
├── migrations
├── permissons.py           权限控制
├── models.py
├── tests.py
├── urls.py
└── views.py

templates
├── base_detail.html        详情信息模板
├── base_list.html          列表模板
├── ClassList.html          班级信息
├── ConultRecord.html       咨询记录
├── Course.html             课程简介
├── CourseRecord.html       上课记录
├── Customer.html           客户记录
├── School.html             校区记录
├── StudyRecord.html        学习记录
├── UserProfile.html        讲师信息
├── lunch.html              基础模板
├── start.html              基础模板
└── login.html              登录

