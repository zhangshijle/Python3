<?php
class HistoryDao extends BaseDao
{
	public function __construct() {
		parent::__construct ();
		$this->tableName = "history";
		$this->table = $this->db->getTDG ( $this->tableName );
		$this->primaryKey = "id";
		$this->db->init ();
	}
}
