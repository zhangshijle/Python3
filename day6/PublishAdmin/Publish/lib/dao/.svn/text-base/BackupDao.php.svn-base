<?php
class BackupDao extends BaseDao
{
	public function __construct() {
		parent::__construct ();
		$this->tableName = "backup";
		$this->table = $this->db->getTDG ( $this->tableName );
		$this->primaryKey = "id";
		$this->db->init ();
	}
}
