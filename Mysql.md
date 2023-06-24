# Mysql

默认端口号：3306

## 初始化

1. 登录:
```
mysql -u root -p
```

2. 退出:
```
exit
```

3. 显示当前数据库的版本信息以及连接用户名：
```
select version(),user();
```

## 数据库

1. 查看数据库:
```
show databases;
```
2. 使用数据库:
```
use xxx;
```
3. 创建数据库:
```
create database xxx;
```
4. 创建数据库:
```
create database xxx;
```
5. 删除数据库:
```
drop database xxx;
```

6. 导入sql文件-"文件路径"（先建立同名数据库）：
```
source xxx.sql;
```


## 数据表
1. 查看数据表:
```
show tables;
```

1. 筛选数据:
```
select * from (表) where xxx='xxx' and xxx='xxx';
```
1. 删除数据：
```
delete from (表) where xxx='xxx';
```
