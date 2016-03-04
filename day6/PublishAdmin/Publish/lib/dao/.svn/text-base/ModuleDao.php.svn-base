<?php
class ModuleDao extends BaseDao 
{
	public function __construct() {
		parent::__construct ();
		$this->tableName = "module";
		$this->table = $this->db->getTDG ( $this->tableName );
		$this->primaryKey = "id";
		$this->db->init ();
	}
}
