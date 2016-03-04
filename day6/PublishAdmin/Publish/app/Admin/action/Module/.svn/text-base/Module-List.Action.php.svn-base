<?php
class ModuleListAction extends ModuleAction
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
//        $this->data["footerJS"] = <<<EOT
//    <script></script>
//EOT;
        $this->data['list'] = $this->getLibObject("ModuleService")->getList();
	}

}
