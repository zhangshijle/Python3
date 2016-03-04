<?php
class ModuleUpdateAction extends ModuleAction 
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
        }


        if($do = $this->context->get('do')){
            $this->$do();
        }

        /*
        $files = $this->getLibObject("FileService")->getModuleUpdateFile($this->data['name']);
        if(!empty($files)){
            $this->confirmUpdate();
        }*/

	}

    public function confirmUpdate(){
        $this->template = strtolower($this->context->uri["module"]) . "-" . strtolower($this->context->get("do"));
        $this->data['templateBtn'] = '

        <h3><p class="text-success">文件上传成功</p><h3>
        <a href="'. C('LtUrl')->generate('Module', 'Update', array('name'=>$this->data['name'], 'do'=>'runUpdate')).'"> <button type="button" class="btn btn-success btn-lg">确认更新此模块</button></a>

        <a href="'. C('LtUrl')->generate('Module', 'Update', array('name'=>$this->data['name'], 'do'=>'runUpdate', 'isBackup'=>true)).'"> <button type="button" class="btn btn-primary btn-lg">确认先备份再更新此模块</button></a>

        <a href="'. C('LtUrl')->generate('Module', 'List').'"> <button type="button" class="btn btn-info btn-lg">取消本次更新，返回到列表页</button></a>
   ';
    }

    public function runUpdate(){

        $this->template = strtolower($this->context->uri["module"]) . "-confirmupdate";
        $files = $this->getLibObject("FileService")->getModuleUpdateFile($this->data['name']);
        $msg = '';
        $this->data['templateBtn'] = '';
        if(empty($files)){
            $msg = '没有找到可更新的文件';
        }else{

            if($this->context->get('isBackup')){


                //备份旧更文件
                $info = $this->getLibObject("ShellService")->doShell($this->data['name'], 'backup');


                $bkMsg = '';
                $bkOut = '';
                if($info['status']===0){
                    $bkMsg = '模块备份操作执行完成！';
                    foreach($info['out'] as $val){
                        $bkOut .= $val."\n";
                    }

                }else{
                    $bkMsg = '模块备份操作未执行！';

                }

                $this->data['templateBtn'] .= '<a> <button type="button" class="btn btn-success btn-lg">'.$bkMsg.'</button></a><br />
       ';
                if($bkOut) $this->data['templateBtn'] .= '<textarea name="content" class="span7" rows="8">'.$bkOut.'</textarea><br />';

            }

            //执行更新远程文件
            $info = $this->getLibObject("ShellService")->doShell($this->data['name'], 'update');

            $msg = '';
            $out = '';
            if($info['status']===0){
                $msg = '模块更新操作执行完成！';
                foreach($info['out'] as $val){
                    $out .= $val."\n";
                }

            }else{
                $msg = '模块更新操作未执行！';

            }
        }

        $this->data['templateBtn'] .= '<a href="'. C('LtUrl')->generate('Module', 'List').'"> <button type="button" class="btn btn-success btn-lg">'.$msg.' 返回到列表页</button></a><br />
   ';

        if($out) $this->data['templateBtn'] .= '<textarea name="content" class="span7" rows="8">'.$out.'</textarea><br />';


    }

    public function cancelUpdate(){

        $files = $this->getLibObject("FileService")->getModuleUpdateFile($this->data['name']);
    }

    public function updateType(){

        $this->template = strtolower($this->context->uri["module"]) . "-confirmupdate";
        $this->data['templateBtn'] = '<a href="'. C('LtUrl')->generate('Module', 'Update', array('name'=>$this->data['name'], 'do'=>'directUpdate')).'"> <button type="button" class="btn btn-success btn-lg">一键发布更新</button></a>

        <a href="'. C('LtUrl')->generate('Module', 'Update', array('name'=>$this->data['name'])).'"> <button type="button" class="btn btn-info btn-lg">上传更新文件</button></a>
   ';

    }

    public function directUpdate(){

        $this->template = strtolower($this->context->uri["module"]) . "-confirmupdate";
        $msg = '';

        //执行更新远程文件
        $info = $this->getLibObject("ShellService")->doShell($this->data['name'], 'update', '-A');

        $msg = '';
        $out = '';
        if($info['status']===0){
            $msg = '模块更新操作执行完成！';
            foreach($info['out'] as $val){
                $out .= $val."\n";
            }

        }else{
            $msg = '模块更新操作未执行！';

        }


        $this->data['templateBtn'] = '<a href="'. C('LtUrl')->generate('Module', 'List').'"> <button type="button" class="btn btn-success btn-lg">'.$msg.' 返回到列表页</button></a><br />
   ';

        if($out) $this->data['templateBtn'] .= '<textarea name="content" class="span7" rows="8">'.$out.'</textarea><br />';



    }


}
