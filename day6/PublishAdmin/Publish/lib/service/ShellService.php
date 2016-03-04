<?php
/**
 * Created by PhpStorm.
 * User: liujian
 * Date: 14-6-13
 * Time: 上午10:49
 */


class ShellService{
    protected $Shell;
    public $module;
    public $action;

    function __construct()
    {
        $this->Shell = '../../publishModules/shell/update.py';
    }

    /**
     * 执行脚本代码
     * @param $module
     * @param $action
     * @return string
     */
    public function doShell($module, $action, $args=''){
        $this->module = $module;
        $this->action = $action;
        $command = $this->getCommand();
        if(!$command) return '执行命令出错';

        if($args)
            $command .= ' '.$args;

        //echo realpath($this->Shell);
        //echo $command;

        exec($command, $out, $status);
        return array('status'=>$status, 'out'=>$out);

        //echo $command.PHP_EOL;
        //return $command ? exec($command) : '执行命令出错';
    }

    /**
     * 生成脚本命令代码
     * @return string
     */
    private function getCommand(){
        $command = $this->Shell;
        // 操作白名单
        $actionList = array(
            "update",               // 更新
            "backup",               // 备份
            "rollback",             // 回滚
            "full_update",          // 完全更新
            "test_update"           // 测试更新
        );

        // 处理模块名
        if($this->module){
            $command .= ' -m ' . strip_tags($this->module);
        }
        else{
            $command = false;
        }

        // 处理操作名
        if($this->action && in_array($this->action, $actionList)){
            $command .= ' -a ' . strip_tags($this->action);
        }
        else{
            $command = false;
        }

        return $command;
    }

    public function getPermissions(){
        return array(
            $this->Shell => array(
                'type' => '可执行',
                'bool' => is_executable($this->Shell)
            )
        );
    }
}