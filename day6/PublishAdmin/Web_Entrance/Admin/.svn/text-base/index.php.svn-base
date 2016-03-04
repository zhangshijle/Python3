<?php
ini_set("display_errors", "1");
// set_magic_quotes_runtime(0);
if (version_compare ( PHP_VERSION, '6.0.0-dev', '<' ) && get_magic_quotes_gpc ()) {
	$in = array (&$_GET, &$_POST, &$_COOKIE, &$_REQUEST );
	while ( list ( $k, $v ) = each ( $in ) ) {
		foreach ( $v as $key => $val ) {
			if (! is_array ( $val )) {
				$in [$k] [$key] = stripslashes ( $val );
				continue;
			}
			$in [] = &$in [$k] [$key];
		}
	}
	unset ( $in );
}
// 引入 LotusPHP
$lotusHome = substr(dirname(__FILE__), 0, strpos(__FILE__, "Web_Entrance"));
include $lotusHome . 'runtime/Lotus.php';
$lotus = new Lotus ();
$lotus->option ["proj_dir"] = $lotusHome . "Publish";
$lotus->option ["app_name"] = "Admin";
$lotus->init ();
