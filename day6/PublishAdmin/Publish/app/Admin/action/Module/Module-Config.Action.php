<?php
class ModuleConfigAction extends ModuleAction
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
//        $this->data["footerJS"] = <<<EOT
//    <script></script>
//EOT;
        if(empty($_POST)){

            if(!$this->getLibObject("moduleService")->isWritableConfig()){

                $this->data['error_messages'][] = array('msg'=>'配置文件不可写');
                $this->data['forward'] = C('LtUrl')->generate('Module', 'Check');
                $this->layout = "resultPage";

            }else{
                $this->data['configs'] = $this->getLibObject("moduleService")->getConfig();
            }

        }else{

            $data['path'] = $this->context->post("data");
            $this->getLibObject("moduleService")->setConfig($data);

            $this->code='200';
            $this->data['forward'] = C('LtUrl')->generate('Module', 'Config');
            $this->layout = "resultPage";

        }





	}
}
