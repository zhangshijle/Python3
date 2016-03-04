<?php
/**
+---------------------------------------------------------------------------+
| Code Backend Generator For Lotus V 1.8.0                                  |
| ========================================================================  |
|                                                                           |
| Copyright (c) 2006-2014 LanMV License MIT                                 |
|                                                                           |
+---------------------------------------------------------------------------+
$Id:
 */

/**
 *
 * @package BackendCodeGenerator.php
 * @author Laoliu <Laoliu@lanmv.com>
 * Lost modified 2014-05-15
 */

// ini_set("display_errors", 0);
// Set timezone
date_default_timezone_set ( 'Etc/GMT-8' );

class BackendCodeGenerator {

    // 默认生成的 Action
    public $_DefaultActions = array (
        "Add", "DoAdd", "Edit", "DoEdit", "Delete", "DoDelete", "Index", "View", "Search", "List"
    );
    public $_Lotus;
    public $_LotusHome;
    public $_ProjectName;
    public $_ProjectHome;
    public $_ProjectRoot;
    public $_AppName;
    public $_AppHome;
    public $_Module;
    public $_ModuleConf;
    public $_ModuleLib;
    public $_Action;
    public $_ModuleAction;
    public $_ModuleActionHome;
    public $_ModuleView;
    public $_ModuleViewHome;
    public $_ExtendsAction;
    public $_InBackend = false;
    public $_CompanyName = '高校邦科技有限公司';

    public function main () {
        if ( 1 == count ( $_SERVER [ 'argv' ] ) ) {
            echo "Usage:
php BackendCodeGenerator.php ProjectName [, AppName] [, Module] [, Action][, ExtendsAction ......]
			
Go to your code generator directory, and then execute:
php CodeGenerator.php ProjectName AppName Module

It equals to:
== Generate ==
(1) php BackendCodeGenerator.php ProjectName AppName Module List 
(2) php BackendCodeGenerator.php ProjectName AppName Module Add
(3) php BackendCodeGenerator.php ProjectName AppName Module DoAdd
(4) php BackendCodeGenerator.php ProjectName AppName Module Edit
(5) php BackendCodeGenerator.php ProjectName AppName Module DoEdit
(6) php BackendCodeGenerator.php ProjectName AppName Module Delete
(7) php BackendCodeGenerator.php ProjectName AppName Module DoDelete
			
*将程序放置在Lotus Runtime 目录。
*参数之间用空格隔开。
";
        }
        else {
            // Lotus Home
            $this->_LotusHome = substr ( dirname ( __FILE__ ), 0, strpos ( __FILE__, "_CodeGenerator" ) );
            $this->_Lotus = $this->_LotusHome . 'Lotus.php';

            // Project Root
            $this->_ProjectRoot = substr ( dirname ( __FILE__ ), 0, strpos ( __FILE__, "runtime" ) );
            $this->_ProjectName = ($_SERVER [ 'argv' ] [ 1 ]) ? $_SERVER [ 'argv' ] [ 1 ] : 'System';
            $this->_ProjectHome = $this->_ProjectRoot . $this->_ProjectName;

            $this->_AppName = ($_SERVER [ 'argv' ] [ 2 ]) ? $_SERVER [ 'argv' ] [ 2 ] : 'Frontend';

            if ( 'Backend' == $this->_AppName ) {
                $this->_InBackend = true;
            }
            $this->_AppHome = $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName;

            $this->_Module = isset ( $_SERVER [ 'argv' ] [ 3 ] ) ? $_SERVER [ 'argv' ] [ 3 ] : 'Admin';
            $this->_ModuleConf = $this->_AppHome . DIRECTORY_SEPARATOR . 'conf';
            $this->_ModuleLib = $this->_AppHome . DIRECTORY_SEPARATOR . 'lib';
            $this->_ModuleAction = $this->_AppHome . DIRECTORY_SEPARATOR . 'action';
            $this->_ModuleActionHome = $this->_ModuleAction . DIRECTORY_SEPARATOR . $this->_Module;
            $this->_ModuleView = $this->_AppHome . DIRECTORY_SEPARATOR . 'view';
            $this->_ModuleViewHome = $this->_ModuleView;

            $this->_Action = isset ( $_SERVER [ 'argv' ] [ 4 ] ) ? $_SERVER [ 'argv' ] [ 4 ] : 'Default-Index';
            $this->_ExtendsAction = ($_SERVER [ 'argv' ] [ 5 ]) ? $_SERVER [ 'argv' ] [ 5 ] : 'LtAction';

            $this->CreateProject ();
        }
    }

    public function CreateProject () {
        if ( !is_dir ( $this->_ProjectHome ) ) {
            echo "01.开始项目初始化 ...\n";
            mkdir ( $this->_ProjectHome );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName, 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'action', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'action' . DIRECTORY_SEPARATOR . '_Component', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'conf', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'dev', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'lib', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'view', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'view' . DIRECTORY_SEPARATOR . 'layout', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'view' . DIRECTORY_SEPARATOR . 'component', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'dev', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'data', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . '3rd_party', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . 'dao', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . 'service', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . 'util', 0777, true );

            // Build Frantend
            if ( !is_dir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' ) ) {
                mkdir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance', 0777, true );
            }
            if ( !is_dir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName ) ) {
                mkdir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName, 0777, true );
            }
            echo "--项目初始化完毕 ...\n";
            echo "02.开始创建项目默认模块 ...\n";
            // 设置默认
            $this->writeDefault ();
        }
        elseif ( !is_dir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName ) ) {
            echo "01.项目已被初始化 ...\n";
            echo "02.开始创建模块 ...\n";
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName, 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'action', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'action' . DIRECTORY_SEPARATOR . '_Component', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'conf', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'dev', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'lib', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'view', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'view' . DIRECTORY_SEPARATOR . 'layout', 0777, true );
            mkdir ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'view' . DIRECTORY_SEPARATOR . 'component', 0777, true );

            // Build Frantend
            if ( !is_dir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' ) ) {
                mkdir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance', 0777, true );
            }
            if ( !is_dir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName ) ) {
                mkdir ( $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName, 0777, true );
            }

            // Write .htaccess
            $Htaccess = $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . '.htaccess';
            file_put_contents ( $Htaccess, "<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
" );

            echo "--创建 Rewrite 创建完毕 ...\n";

            $FrandentIndexFileName = $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'index.php';
            file_put_contents ( $FrandentIndexFileName, "<?php
ini_set(\"display_errors\", \"1\");
date_default_timezone_set(\"Asia/Shanghai\");
// set_magic_quotes_runtime(0);
if (version_compare ( PHP_VERSION, '6.0.0-dev', '<' ) && get_magic_quotes_gpc ()) {
	\$in = array (&\$_GET, &\$_POST, &\$_COOKIE, &\$_REQUEST );
	while ( list ( \$k, \$v ) = each ( \$in ) ) {
		foreach ( \$v as \$key => \$val ) {
			if (! is_array ( \$val )) {
				\$in [\$k] [\$key] = stripslashes ( \$val );
				continue;
			}
			\$in [] = &\$in [\$k] [\$key];
		}
	}
	unset ( \$in );
}
// 引入 LotusPHP
\$lotusHome = substr(dirname(__FILE__), 0, strpos(__FILE__, \"Web_Entrance\"));
include \$lotusHome . 'runtime/Lotus.php';
\$lotus = new Lotus ();
\$lotus->option [\"proj_dir\"] = \$lotusHome . \"" . $this->_ProjectName . "\";
\$lotus->option [\"app_name\"] = \"" . $this->_AppName . "\";
\$lotus->init ();
" );

            echo "--创建前台 index.php 入口文件 ...\n";

            // Write Default-Index.Action.php
            $DefaultModuleFile = $this->_ModuleAction . DIRECTORY_SEPARATOR . 'Default-Index.Action.php';
            file_put_contents ( $DefaultModuleFile, "<?php
class DefaultIndexAction extends " . $this->_ExtendsAction . " {
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
		/**
		 * @todo Code here ...
		**/
	}
}
" );

            echo "--创建默认 Default-Index.Action.php 文件 ...\n";

            $DefaultModuleViewFile = $this->_ModuleView . DIRECTORY_SEPARATOR . 'default-index.php';
            file_put_contents ( $DefaultModuleViewFile, "<div>Lotus 已经安装，你可以开始使用她啦 ...</div>" );

            echo "--创建默认视图 default-index.php 文件 ...\n";

            // 写入AppLib文件
            $this->writeAppLib ();
        }
        else {
            echo "01.项目已被初始化 ...\n";
            echo "02.开始创建模块 ...\n";
            $this->CreateModule ();
        }
    }

    public function CreateModule () {
        if ( !is_dir ( $this->_ModuleActionHome ) ) {
            echo "03.开始创建模块目录 ...\n";
            mkdir ( $this->_ModuleActionHome, 0777, true );
            if ( !is_dir ( $this->_ModuleViewHome ) ) {
                mkdir ( $this->_ModuleViewHome, 0777, true );
            }
            if ( !is_dir ( $this->_ModuleConf ) ) {
                mkdir ( $this->_ModuleConf, 0777, true );
            }
            if ( !is_dir ( $this->_ModuleLib ) ) {
                mkdir ( $this->_ModuleLib, 0777, true );
            }
            echo "--模块目录创建完毕 ...\n";
        }
        if ( '_DA' == $this->_Action ) {
            echo "04.Action为空，用默认Action数组值创建多个Action ...  \n";
            foreach ( $this->_DefaultActions as $Action ) {
                $this->writeModuleAction ( $this->_Module, $Action );
                $this->writeModuleView ( $this->_Module, $Action );
            }
            echo "创建" . $this->_ProjectName . '-' . $this->_AppName . '-' . $this->_Module . "完毕...\n";
        }
        else {
            echo "04.开始创建Module和Action ...\n";
            $this->writeModuleAction ( $this->_Module, $this->_Action );
        }

        $this->writeDAO ( $this->_Module );
        echo "==== 项目创建完毕 ...\n";
    }

    public function writeModuleAction ( $Module, $Action ) {
        $ActionExecute = '';
        if ( $Module && $Action ) {
            $thisModule = $Module;
            $thisAction = $Action;
        }
        else {
            $thisModule = $this->_Module;
            $thisAction = $this->_Action;
        }
        $ActionName = $this->_ModuleActionHome . DIRECTORY_SEPARATOR . $thisModule . '-' . $thisAction . '.Action.php';
        if ( $thisModule != 'Api' ) {
            if ( $this->_InBackend ) {
                if ( 'Add' == $thisAction ) {
                    $ActionExecute = '
		if ( $this->FIELDS ) {
			// 生成表单
			$this->TAG->FIELDSCONFIG = $this->FIELDS;
			$formConfig = array (
				"URL" => C ( "LtURL" )->generate ( $this->context->uri [ "module" ], "Do" . $this->context->uri [ "action" ] ) 
			);
			$this->data [ "HTML" ] = $this->TAG->buildForm ( $formConfig );
		}
		else {
			$this->data [ "HTML" ] = \'<h4>未找到数据字典</h4><br /><a class="btn btn-mini" href="\' . C ( "LtURL" )->generate ( "Fields", "Add" ) .\'">转至配置数据字典</a>\';
		}
';
                }
                elseif ( 'Edit' == $thisAction ) {
                    $ActionExecute = '
		if ( $this->FIELDS ) {
			// 获取编辑内容序号
			$id = intval ( $this->context->get ( "ID" ) );
			// 操作数据表
			$Content = $this->DAO->get ( $id );
			if ( $Content ) {
				// 生成表单
				$this->TAG->FIELDSVALUE = $Content;
				$formConfig = array (
					"URL" => C ( "LtURL" )->generate ( $this->context->uri [ "module" ], "Do" . $this->context->uri [ "action" ] ) 
				);
				$this->data [ "HTML" ] = $this->TAG->buildForm ( $formConfig );
			}
		}
		else {
			$this->data [ "HTML" ] = \'<h4>未找到数据字典</h4><br /><a class="btn btn-mini" href="\' . C ( "LtURL" )->generate ( "Fields", "Add" ) . \'">转至配置数据字典</a>\';
		}
';
                }
                elseif ( 'View' == $thisAction ) {
                    $ActionExecute = '
		// 列表表单
		$id = intval ( $this->context->get ( "ID" ) );
		$this->data [ "Rows" ] = $this->DAO->get ( $id );
';
                }
                elseif ( 'DoAdd' == $thisAction ) {
                    $ActionExecute = '
		$data = $_POST [ "data" ];
		$insertId = $this->DAO->insert ( $data );
		if ( $insertId ) {
			$this->code = 200;
			$this->data [ "forward" ] = C ( "LtUrl" )->generate ( $this->context->uri [ "module" ], "Add" );
		}
		else {
			$this->code = 405;
			$this->data [ "forward" ] = "goback";
		}
';
                }
                elseif ( 'DoEdit' == $thisAction ) {
                    $ActionExecute = '
		$data = $_POST [ "data" ];
		$updated = $this->DAO->update ( $data );
		if ( $updated ) {
			$this->code = 200;
			$this->data [ "forward" ] = C ( "LtUrl" )->generate ( $this->context->uri [ "module" ], "List" );
		}
		else {
			$this->code = 405;
			$this->data [ "forward" ] = "goback";
		}
';
                }
                elseif ( 'DoDelete' == $thisAction ) {
                    $ActionExecute = '
		$id = intval ( $this->context->get ( "ID" ) );
		$deleted = $this->DAO->del ( $id );
		if ( $deleted ) {
			$this->code = 200;
			$this->data [ "forward" ] = C ( "LtUrl" )->generate ( $this->context->uri [ "module" ], "List" );
		}
		else {
			$this->code = 405;
			$this->data [ "forward" ] = C ( "LtUrl" )->generate ( $this->context->uri [ "module" ], "List" );
		}
';
                }
                elseif ( 'Api' == $thisAction ) {
                    $ActionExecute = '
		$this->SERVICE = new ' . $thisModule . 'Service ();
		$publishService = array (
			"method1", "method2", "method3"
		);
		$this->OhServer->addMethods ( $publishService, new $this->SERVICE () );
		//$this->OhServer->setDebugEnabled ( true );
		$this->OhServer->handle ();
';
                }
                elseif ( 'List' == $thisAction ) {
                    $ActionExecute = '
		// 占位
';
                }
                else {
                    $ActionExecute = '';
                }
            }

            file_put_contents ( $ActionName, "<?php
class " . $thisModule . $thisAction . "Action extends " . $this->_ExtendsAction . " 
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
" . $ActionExecute . "
	}
}
" );
        }
        else {
            file_put_contents ( $ActionName, "<?php
class " . $thisModule . $thisAction . "Action extends " . $this->_ExtendsAction . " 
{
	public function __construct() {
		parent::__construct ();
		\$this->DAO = new " . $thisAction . "Dao ();
	}
	
	public function execute() {
		\$this->OhServer->add( array( 'Add', 'Get', 'Update', 'Delete' ), new " . $thisModule . $thisAction . "Action () );
		\$this->OhServer->start();
	}
}
" );
            $this->writeDAO ( $thisModule );
            $this->writeService ( $thisModule );
        }
        echo "-- Module: $thisModule and Action: $thisAction 创建完毕, 开始创建 Module View ...\n";
        if ( $thisModule != 'Api' ) {
            $this->writeModuleView ( $thisModule, $thisAction );
        }
    }

    public function writeModuleView ( $Module, $Action ) {
        $ViewFile = $this->_ModuleViewHome . DIRECTORY_SEPARATOR . strtolower($Module) . '-' . strtolower($Action) . '.php';

        if ( $this->_InBackend ) {
            if ( in_array ( $Action, array (
                'add', 'edit'
            ) ) ) {
                $ActionView = '{component Form Build}';
            }
            elseif ( in_array ( $Action, array (
                'list', 'search', 'index'
            ) ) ) {
                $ActionView = '{component Table List}';
            }
            else {
                $ActionView = "<div>This is Module: $Module - Action: $Action</div>";
            }
        }
        else {
            $ActionView = "<div>This is Module: $Module - Action: $Action</div>";
        }

        file_put_contents ( $ViewFile, $ActionView );
    }

    public function writeDAO ( $Module ) {
        $DaoFileName = $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . 'dao' . DIRECTORY_SEPARATOR . ucwords ( $Module ) . 'Dao.php';
        if ( !file_exists ( $DaoFileName ) ) {
            $tableName = strtolower ( $Module );
            file_put_contents ( $DaoFileName, "<?php
class " . $Module . "Dao extends BaseDao 
{
	public function __construct() {
		parent::__construct ();
		\$this->tableName = \"" . $tableName . "\";
		\$this->table = \$this->db->getTDG ( \$this->tableName );
		\$this->primaryKey = \"id\";
		\$this->db->init ();
	}
}
" );
            echo "05.DAO文件创建完毕 ...";
        }
        else {
            echo $Module . "05.DAO文件已存在, 跳过 ...\n";
        }
    }

    public function writeService ( $Module ) {
        $Module = ucwords($Module);
        $ServiceFileName = $this->_ProjectHome . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . 'service' . DIRECTORY_SEPARATOR . ucwords ( $Module ) . 'Service.php';
        if ( !file_exists ( $ServiceFileName ) ) {
            $tableName = strtolower ( $Module );
            file_put_contents ( $DaoFileName, "<?php
class " . $Module . "Service {
	public \$" . $Module . "DAO;
	public function __construct() {
		parent::__construct ();
		\$this->" . $Module . "DAO = new \"" . $Module . "Dao ()\";
	}
	
	public function example() {
		return true;	
	}
}
" );
            echo "06.Service文件创建完毕 ...";
        }
        else {
            echo $Module . "06.Service文件已存在, 跳过 ...\n";
        }
    }

    public function writeAppLib () {
        $AppLibFileName = $this->_ProjectHome . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . $this->_AppName . 'Action.php';
        if ( !file_exists ( $AppLibFileName ) ) {
            if ( 'Backend' == $this->_AppName ) {
                file_put_contents ( $AppLibFileName, '<?php
class BackendAction extends LtAction {
  public $MODEL, $MODELNAME, $FIELDS, $FIELDHEAD = array ();
  public $OhClient, $OhServer, $AUTH, $TAG, $DAO;

  public function __construct () {
    parent::__construct ();
    $this->Auth = new BaseAuth ();
  }

  public function beforeExecute () {
    // 定义Hprose Server
    $this->OhClient = new HproseHttpClient ();
    $this->OhServer = new HproseHttpServer();
    // 定义 MVC
    $this->responseType = \'tpl\';
    $this->layout = (\'Do\' == substr ( $this->context->uri [ \'action\' ], 0, 2 )) ? \'resultPage\' : \'defaultPage\';
    $this->data [ \'baseurl\' ] = ($baseURL = LtObjectUtil::singleton ( \'LtConfig\' )->get ( \'baseurl\' )) ? $baseURL : \'/\';
    $this->data [ \'_pages\' ] = $this->data [ \'title\' ] = $this->data [ \'PageTitle\' ] = \'\';
    // 设置表单生成器 Form
    if ( in_array ( $this->context->uri [ \'action\' ], array (
      "Edit", "Add" 
    ) ) ) {
      $this->TAG = new TagService ();
    }
    // 处理菜单
    $MENUSVC = new MenuService ();
    $MENUSVC->MODULE = $this->context->uri [ \'module\' ];
    $MENUSVC->ACTION = $this->context->uri [ \'action\' ];
    $this->data [ \'topMenus\' ] = $MENUSVC->getTopMenus ();
    $this->data [ \'leftMenus\' ] = $MENUSVC->getLeftMenus ();
    // 取出数据模型及字段
    $MODEL = new ModelService ();
    $this->MODEL = $MODEL->getRowByModelName ( $this->context->uri [ \'module\' ] );
    if ( isset ( $this->MODEL [ \'id\' ] ) ) {
      // 数据库操作
      $modelDao = $this->context->uri [ \'module\' ] . \'Dao\';
      $this->DAO = new $modelDao ();
      // 取出字段数据
      $FIELDS = new FieldService ();
      $this->FIELDS = $FIELDS->getRowByModelId ( $this->MODEL [ \'id\' ] );
      $this->FIELDHEAD = $FIELDS->getRowForTableHead ( $this->MODEL [ \'id\' ] );
      // 设置 表单生成器
      if ( is_object ( $this->TAG ) ) {
        $this->TAG->FIELDSCONFIG = $this->FIELDS;
        $this->TAG->FORMACTION = $this->context->uri [ \'action\' ];
        $this->TAG->MODELID = $this->context->uri [ \'module\' ];
        $this->TAG->MODELNAME = $this->MODEL [ \'modelTitle\' ];
      }
      $this->data [ \'PageTitle\' ] = $this->MODEL [ \'modelTitle\' ];
    }

    // 为设置内容模型时如下处理
    $this->data [ \'_table\' ] = $this->data [ \'HTML\' ] = \'<h4>未找到数据字典</h4><br /><a class="btn btn-mini" href="\' . C ( "LtURL" )->generate ( "Fields", "Add" ) . \'">转至配置数据字典</a>\';
    
    // 设置表格生成器 Table
    if ( in_array ( $this->context->uri [ \'action\' ], array (
      "List", "Index" 
    ) ) && isset ( $this->MODEL [ \'id\' ] ) ) {
      // 数据字典配置
      $FieldSvc = new FieldService ();
      $queryFields = $FieldSvc->genQueryField ( $this->FIELDHEAD );
      // 计算分页
      $page = $this->context->get ( \'Page\' );
      $page = max ( intval ( $page ), 1 );
      $page_size = LtObjectUtil::singleton ( \'LtConfig\' )->get ( \'page_size\' );
      if ( empty ( $page_size ) ) $page_size = 25;
      $limit = $page_size;
      $offset = ($page - 1) * $page_size;
      // 表单配置
      $TABLE = new Table ();
      $TABLE->MODEL = $this->context->uri [ \'module\' ];
      $TABLE->TABLEHEAD = $this->FIELDHEAD;
      $TABLE->FIELDCONFIG = $this->FIELDS;
      $TABLE->CONTENT = $this->DAO->getByFieldName ( $queryFields, $limit, $offset, null, true );
      $count = $this->DAO->countByFieldName ( $queryFields, $limit, $offset, null, true );
      if ( $count > $page_size ) {
        // 生成分页
        $URL = new LtUrl ();
        $URL->init ();
        $base_url = $URL->generate ( $this->context->uri [ \'module\' ], $this->context->uri [ \'action\' ], array (
          \'Page\' => \':page\' 
        ) );
        $pagination = new LtPagination ();
        $pagination->init ();
        // 模板赋值
        $this->data [ \'_pages\' ] = $pagination->pager ( $page, $count, $base_url );
      }
      $this->data [ \'_table\' ] = $TABLE->genTag ();
    }
      
    // 处理 Title
    $this->data [ \'title\' ] = ($this->context->uri [ \'module\' ] == \'Default\' && !isset ( $this->MODEL [ \'modelTitle\' ] )) ? \'Smart Cloud Platforms v1.0.0\' : $this->MODEL [ \'modelTitle\' ] . \'管理 - Smart Cloud Platforms v1.0.0\';
  }
}' );
            }
            else {
                file_put_contents ( $AppLibFileName, '<?php
class ' . $this->_AppName . 'Action extends LtAction {
	public function __construct() {
		parent::__construct ();
	}
	
	public function beforeExecute() {
		// layout setting
		$this->responseType = "tpl";
		$layout = "Do" == substr ( $this->context->uri ["action"], 0, 2 ) ? "resultPage" : "defaultPage";
		$this->layout = $layout;
		$this->data ["baseurl"] = ($baseURL = LtObjectUtil::singleton ( "LtConfig" )->get ( "baseurl" )) ? $baseURL : "/";
		
		$this->data ["title"] = "' . $this->_CompanyName . '";
	}
}
				' );
            }
        }
    }

    public function writeDefault () {
        $FrandentIndexFileName = $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . 'index.php';
        file_put_contents ( $FrandentIndexFileName, "<?php
ini_set(\"display_errors\", \"1\");
// set_magic_quotes_runtime(0);
if (version_compare ( PHP_VERSION, '6.0.0-dev', '<' ) && get_magic_quotes_gpc ()) {
	\$in = array (&\$_GET, &\$_POST, &\$_COOKIE, &\$_REQUEST );
	while ( list ( \$k, \$v ) = each ( \$in ) ) {
		foreach ( \$v as \$key => \$val ) {
			if (! is_array ( \$val )) {
				\$in [\$k] [\$key] = stripslashes ( \$val );
				continue;
			}
			\$in [] = &\$in [\$k] [\$key];
		}
	}
	unset ( \$in );
}
// 引入 LotusPHP
\$lotusHome = substr(dirname(__FILE__), 0, strpos(__FILE__, \"Web_Entrance\"));
include \$lotusHome . 'runtime/Lotus.php';
\$lotus = new Lotus ();
\$lotus->option [\"proj_dir\"] = \$lotusHome . \"" . $this->_ProjectName . "\";
\$lotus->option [\"app_name\"] = \"" . $this->_AppName . "\";
\$lotus->init ();
" );

        echo "--创建前台 index.php 入口文件 ...\n";

        // 默认配置索引文件
        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'conf.php', "<?php
// 读取standard配置, 并覆盖共享配置的部分配置。
foreach(glob(dirname(__FILE__) . '/standard/*.php') as \$confFile){
	if (__FILE__ != \$confFile){
		include(\$confFile);
	}
}
return \$config;" );

        // 默认开发模式下配置索引文件
        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'conf_dev.php', "<?php
// 开发模式下先读取standard配置, 然后读取dev配置,并覆盖standard的部分配置
include(dirname(__FILE__) . '/conf.php');
// 读取dev配置
foreach(glob(dirname(__FILE__) . '/dev/*.php') as \$confFile){
	if (__FILE__ != \$confFile){
		include(\$confFile);
	}
}
return \$config;" );

        // 数据库配置文件
        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard' . DIRECTORY_SEPARATOR . 'db.conf.php', "<?php
// Build DB Config array 
\$dbConfigBuild = new LtDbConfigBuilder;
// 部署分布式数据库
\$dbConfigBuild->addHost(\"" . $this->_ProjectName . "\", \"" . $this->_AppName . "\", \"master\", array(\"adapter\" => \"pdo_mysql\", \"host\" => 'localhost', \"port\" => '', \"password\" => \"123456\", \"dbname\" => 'projectdb'));
\$dbConfigBuild->addHost(\"" . $this->_ProjectName . "\", \"" . $this->_AppName . "\", \"slave\", array(\"adapter\" => \"pdo_mysql\", \"host\" => 'localhost', \"port\" => '', \"password\" => \"123456\", \"dbname\" => 'projectdb'));
// 指定数据库配置数组
\$config[\"db.servers\"] = \$dbConfigBuild->getServers();
" );

        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'dev' . DIRECTORY_SEPARATOR . 'db.conf.php', "<?php
// Build DB Config array
\$dbConfigBuild = new LtDbConfigBuilder;
// 部署分布式数据库
\$dbConfigBuild->addHost(\"" . $this->_ProjectName . "\", \"" . $this->_AppName . "\", \"master\", array(\"adapter\" => \"pdo_mysql\", \"host\" => 'localhost', \"port\" => '', \"password\" => \"123456\", \"dbname\" => 'projectdb'));
\$dbConfigBuild->addHost(\"" . $this->_ProjectName . "\", \"" . $this->_AppName . "\", \"slave\", array(\"adapter\" => \"pdo_mysql\", \"host\" => 'localhost', \"port\" => '', \"password\" => \"123456\", \"dbname\" => 'projectdb'));
// 指定数据库配置数组
\$config[\"db.servers\"] = \$dbConfigBuild->getServers();
" );

        // 系统缓存配置文件
        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard' . DIRECTORY_SEPARATOR . 'cache.conf.php', "<?php
\$ccb = new LtCacheConfigBuilder;
\$ccb->addSingleHost( array (\"adapter\" => \"phps\",
		\"host\" => \"/tmp/LanMV/Cache-phps/\"
		));
\$config[\"cache.servers\"] = \$ccb->getServers();" );

        // Cookie 密钥配置文件
        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard' . DIRECTORY_SEPARATOR . 'cookie.conf.php', "<?php
\$config['cookie.secret_key'] = 'ZY)&%$!@$(#*';" );

        // 验证码配置文件
        file_put_contents ( $this->_ProjectHome . DIRECTORY_SEPARATOR . 'conf' . DIRECTORY_SEPARATOR . 'standard' . DIRECTORY_SEPARATOR . 'captcha.conf.php', "<?php
// 验证码
\$config['captcha.seed_file_root'] = \"/tmp/Lotus/captcha/seed/\";
\$config['captcha.allow_chars'] = \"23456789abcdeghkmnpqsuvxyz\";
\$config['captcha.length'] = 4;
\$config['captcha.image_engine'] = 'LtCaptchaImageEngine';
\$config['captcha.image_engine_conf'] = array('blur' => false,
	'scale' => 2,
	'width' => 200,
	'height' => 80,
	'max_rotation' => 4,
	);" );

        echo "--创建 系统默认配置文件 创建完毕 ...\n";

        // Write .htaccess
        $Htaccess = $this->_ProjectRoot . DIRECTORY_SEPARATOR . 'Web_Entrance' . DIRECTORY_SEPARATOR . $this->_AppName . DIRECTORY_SEPARATOR . '.htaccess';
        file_put_contents ( $Htaccess, "<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
" );

        echo "--创建 Rewrite 创建完毕 ...\n";

        // Write Default-Index.Action.php
        $DefaultModuleFile = $this->_ModuleAction . DIRECTORY_SEPARATOR . 'Default-Index.Action.php';
        file_put_contents ( $DefaultModuleFile, "<?php
class DefaultIndexAction extends " . $this->_ExtendsAction . " {
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
		/**
		 * @todo Code here ...
		**/
	}
}
" );

        echo "--创建默认 Default-Index.Action.php 文件 ...\n";

        $DefaultModuleViewFile = $this->_ModuleView . DIRECTORY_SEPARATOR . 'Default-Index.php';
        file_put_contents ( $DefaultModuleViewFile, "<div>Lotus 已经安装，你可以开始使用她啦 ...</div>" );

        echo "--创建默认视图 Default-Index.php 文件 ...\n";

        $this->CreateModule ();
    }
}

$CodeGenerator = new BackendCodeGenerator();
$CodeGenerator->main ();
