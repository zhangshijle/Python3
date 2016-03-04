<?php
class ModuleBackupAction extends ModuleAction 
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {

        $this->data['name'] = $this->context->get('name');

        if(!$this->data['name']){
            $this->data['forward'] = 'goback';
            $this->code = 403;
            $this->layout = "resultPage";
            return;
        }

        //备份旧更文件
        $info = $this->getLibObject("ShellService")->doShell($this->data['name'], 'backup');

        $msg = '';
        $out = '';
        if($info['status']===0){
            $msg = '模块备份操作执行完成！';
            foreach($info['out'] as $val){
                $out .= $val."\n";
            }

        }else{
            $msg = '模块备份操作未执行！';

        }


        $this->data['templateBtn'] = '<a href="'. C('LtUrl')->generate('Module', 'List').'"> <button type="button" class="btn btn-success btn-lg">'.$msg.' 返回到列表页</button></a><br />
   ';
        if($out) $this->data['templateBtn'] .= '<textarea name="content" class="span7" rows="8">'.$out.'</textarea><br />';


    }
}
