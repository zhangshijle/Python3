<?php
class ModuleCheckAction extends ModuleAction
{
	public function __construct() {
		parent::__construct ();
	}
	
	public function execute() {

        $permissions = array();
        $servers = array('FileService', 'ModuleService', 'ShellService');
        foreach($servers as $s){
            $permissions += $this->getLibObject($s)->getPermissions();
        }

        $this->data['permissions'] = $permissions;

	}
}
