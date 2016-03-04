<?php
// Build DB Config array 
$dbConfigBuild = new LtDbConfigBuilder;
// 部署分布式数据库
$dbConfigBuild->addHost("WebIM", "Backend", "master", array(
    "adapter" => "pdo_mysql",
    "host" => '10.0.247.179',
    "port" => '3306',
    "password" => "123456",
    "username" => 'odd_user',
    "dbname" => 'odd_db'
));
$dbConfigBuild->addHost("WebIM", "Backend", "slave", array(
    "adapter" => "pdo_mysql",
    "host" => '10.0.247.179',
    "port" => '3306',
    "password" => "123456",
    "username" => 'odd_user',
    "dbname" => 'odd_db'
));
// 指定数据库配置数组
$config["db.servers"] = $dbConfigBuild->getServers();
