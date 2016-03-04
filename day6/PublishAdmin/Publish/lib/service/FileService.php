<?php
/**
 * Created by PhpStorm.
 * User: liujian
 * Date: 14-6-13
 * Time: 上午10:48
 */


class FileService{

    public function getModuleUpdateFile($mod){

        $module = new ModuleService();
        if($module->isWritableConfig()){
            $configs = $module->getConfig();

            if(isset($configs['path']['upload_path']))
                return  glob($configs['path']['upload_path'].'/'.$mod.'.*');
        }

        return array();

    }

    public function getPermissions(){

        $module = new ModuleService();

        if(!$module->isWritableConfig()) return array();

        $configs = $module->getConfig();

        if(empty($configs['path'])) return array();

        $permissions = array();
        foreach($configs['path'] as $path){
            $permissions[$path] = array(
                'type' => '可写',
                'bool' => is_writable($path)
            );
        }

        return $permissions;
    }

}