<?php
// Build DB Config array 
$dbConfigBuild = new LtDbConfigBuilder;
// 部署分布式数据库
$dbConfigBuild->addHost("Publish", "Admin", "master", array("adapter" => "pdo_mysql", "host" => 'localhost', "port" => '', "password" => "123456", "dbname" => 'projectdb'));
$dbConfigBuild->addHost("Publish", "Admin", "slave", array("adapter" => "pdo_mysql", "host" => 'localhost', "port" => '', "password" => "123456", "dbname" => 'projectdb'));
// 指定数据库配置数组
$config["db.servers"] = $dbConfigBuild->getServers();
