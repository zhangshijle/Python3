<?php
$ccb = new LtCacheConfigBuilder;
$ccb->addSingleHost( array ("adapter" => "phps",
		"host" => "/tmp/LanMV/Cache-phps/"
		));
$config["cache.servers"] = $ccb->getServers();