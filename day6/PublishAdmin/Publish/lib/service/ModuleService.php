<?php
/**
 * Created by PhpStorm.
 * User: liujian
 * Date: 14-6-16
 * Time: 下午4:53
 */

class ModuleService{

    private $_mod_file='../../publishModules/shell/mod.ini';
    private $_mod_file_exclude='../../publishModules/shell/exclude.txt';
    private $_config_file = '../../publishModules/shell/config.ini';

    public function Add($name, $data){

        $ini = $this->array2ini($data, $name);

        file_put_contents($this->_mod_file, $ini, FILE_APPEND);

    }

    public function Update($name, $data){
        $org_ini = $this->getList();
        $org_ini[$name] = array_merge($org_ini[$name], $data);

        $ini = $this->array2ini($org_ini);
        file_put_contents($this->_mod_file, $ini);

    }

    public function getList(){
        return parse_ini_file($this->_mod_file, true,$scanner_mode = INI_SCANNER_RAW);
    }

    public function array2ini($array, $name=""){
        $ini = '';
        if($name) $ini = "[$name]\n";
        foreach($array as $key=>$value){
            if(is_array($value)){
                $ini .= $this->array2ini($value, $key);
            }elseif(!empty($value)){
                $ini .= "$key = $value\n";
            }
        }
        return $ini."\n\n";
    }

    public function getExclude(){
        return file_get_contents($this->_mod_file_exclude);
    }

    public function setExclude($content){
        file_put_contents($this->_mod_file_exclude, $content);
    }

    public function setConfig($configs){
        $config_ini = $this->array2ini($configs);
        file_put_contents($this->_config_file, $config_ini);
    }

    public function getConfig(){
        return parse_ini_file($this->_config_file, true);
    }

    public function isWritableConfig(){
        return is_writable($this->_config_file);
    }


    public function getPermissions(){
        return array(
            $this->_mod_file => array(
                'type' => '可写',
                'bool' => is_writable($this->_mod_file)
            ),
            $this->_mod_file_exclude => array(
                'type' => '可写',
                'bool' => is_writable($this->_mod_file_exclude)
            ),
            $this->_config_file => array(
                'type' => '可写',
                'bool' => is_writable($this->_config_file)
            ),
        );
    }

}
