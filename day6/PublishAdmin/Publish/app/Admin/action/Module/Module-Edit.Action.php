<?php
class ModuleEditAction extends ModuleAction
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {
//        $this->data["footerJS"] = <<<EOT
//    <script></script>
//EOT;
        if(empty($_POST)){
            $name = $this->context->get('name');

            $ini = $this->getLibObject("moduleService")->getList();

            if(!isset($ini[$name])){
                $this->data['forward'] = 'goback';
                $this->code = 403;
                $this->layout = "resultPage";
            }else{
                $this->data['data'] = $ini[$name];
                $this->data['name'] = $name;
            }

            return;

        };
        $ret = array();
        $name = trim($this->context->post("name"));

        $msg = '';

        $ret['status'] = false;
        $this->data['forward'] = 'goback';
        if(empty($name)){
            $msg = array('msg'=>'请填写模块名称');
        }else{
            $data = $this->context->post('data');

            if(empty($data['path']) || empty($data['ip'])){
                $msg = array('msg'=>'请填写部署路径或服务器IP');
            }else{
                $ret['status'] = true;

                $data_more = trim($this->context->post('data_more'));
                if($data_more){

                    $marr = explode("\n", $data_more);
                    foreach($marr as $val){
                        list($k,$v) = explode("=", $val);
                        if(trim($k) && trim($v)){
                            $data[trim($k)] = trim($v);
                        }
                    }

                }

            }

        }

        if($ret['status']){

            $this->code='200';
            $this->getLibObject("moduleService")->update($name, $data);
            $this->data['forward'] = C('LtUrl')->generate('Module', 'List');

        }

        if($msg) $this->data['error_messages'][] = $msg;
        $this->layout = "resultPage";

	}
}
