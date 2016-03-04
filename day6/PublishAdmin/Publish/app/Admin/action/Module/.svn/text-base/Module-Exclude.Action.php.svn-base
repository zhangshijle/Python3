<?php
class ModuleExcludeAction extends ModuleAction
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
//        $this->data["footerJS"] = <<<EOT
//    <script></script>
//EOT;
        if(empty($_POST)){

            $this->data['excludeContent'] = $this->getLibObject("moduleService")->getExclude();
            return;
        }

        $ret = array();
        $content = trim($this->context->post("content"));
        $this->getLibObject("moduleService")->setExclude($content);

        $this->code='200';
        $this->data['forward'] = C('LtUrl')->generate('Module', 'Exclude');
        $this->layout = "resultPage";

	}
}
