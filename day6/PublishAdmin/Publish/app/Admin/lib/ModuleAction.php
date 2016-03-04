<?php
class ModuleAction extends LtAction {

    private $_libObjects = array();

	public function __construct() {
		parent::__construct ();
	}

    public function getLibObject($objectName){

        if(!isset($this->_libObjects[$objectName]) || !is_object($this->_libObjects[$objectName]))
            $this->_libObjects[$objectName] = new $objectName();

        return $this->_libObjects[$objectName];
    }
	
	public function beforeExecute() {
		// layout setting
		$this->responseType = "tpl";
		$layout = "Do" == substr ( $this->context->uri ["action"], 0, 2 ) ? "resultPage" : "defaultPage";
		$this->layout = $layout;
		$this->data ["baseurl"] = ($baseURL = LtObjectUtil::singleton ( "LtConfig" )->get ( "baseurl" )) ? $baseURL : "/";
		$this->data ["HtmlEditor"] = null;
		$this->data ["topMenus"] = null;
        $this->data ["footerJS"] = null;
		$this->data ["title"] = ($layout == "resultPage") ? "操作提示" : "运维管理";

        $this->data['moduleType'] = array('java','jar', 'php', 'c');
	}

    
}
				