<?php

/**
 * @package		BaseDao.php
 * @author		Liujian <liujian@izptec.com>
 * LostModified	2014-05-16
 */

class BaseDao {
    /**
     * 操作数据表
     * @var LtDbTableDataGateway
     */
    protected $table;

    /**
     * @var 数据表名
     */
    protected $tableName;

    /**
     * 数据表主键
     * @var string
     */
    protected $primaryKey;

    /**
     * 数据表操作对象
     * @var LtDbHandle
     */
    protected $dbh;

    /**
     * SQLMapClient
     * @var LtDbSqlMapClient
     */
    protected $smc;

    /**
     * 数据库操作类
     * @var LtDb
     */
    protected $db;

    /**
     * Cachehandler
     * @var Cachehandler
     */
    protected $cache;

    /**
     * @var CacheTableDataGateway
     */
    protected $cacheTDG;

    /**
     * 缓存类型
     * @var string
     */
    protected $cacheType;

    /**
     * @var 缓存时间
     */
    protected $cacheTime;

    /**
     * 是否启用缓存
     * @var bool
     */
    protected $enableCache = false;

    public function __construct () {
        $this->db = new LtDb();
        $this->db->group = "Backend";
        $this->db->node = "Search";
        $this->db->init ();

        // 启用Cache
        $Cache = new LtCache ();
        $Cache->configHandle->get ( "cache.servers" );
        $Cache->group = 'Backend';
        $Cache->node = 'Search';
        $Cache->init ();
        $this->cache = $Cache->getTDG ( "Basedao" );
        $this->cacheTime = ($this->cacheTime) ? $this->cacheTime : 3600;

        $this->dbh = $this->db->getDbHandle ();
        $this->smc = $this->db->getSqlMapClient ();
    }

    /**
     * 插入数据
     * @param array $data
     * @return int lastInsertId
     */
    public function insert ( $data ) {
        return $this->table->insert ( $data );
    }

    /**
     * 根据主键进行更新数据
     * @param array $data
     * @return bool
     */
    public function update ( $data ) {
        $primaryKey = $this->primaryKey;
        $primaryKeyId = $data [ $primaryKey ];
        unset ( $data [ $primaryKey ] );
        return $this->table->update ( $primaryKeyId, $data );
    }

    /**
     * 按 $condition 条件更新
     * @example $condition = array('expression' => 'id < :id', 'value' => array('id' => 10));
     * @param array $data
     * @param array $condition
     * @return bool
     */
    public function updateRow ( $condition, $data ) {
        return $this->table->updateRows ( $condition, $data );
    }

    /**
     * 按主键查询
     * @param integer $primaryKeyId
     * @return array
     */
    public function get ( $primaryKeyId ) {
        return $this->table->fetch ( $primaryKeyId );
    }

    /**
     * 按条件查询
     * @example $condition['where'] = array('expression' => 'id < :id', 'value' => array('id' => 10));
     * @param array $condition
     * @return array
     */
    public function getRow ( $condition = null ) {
        $result = array();
        $cacheKey = '';
        $condition = (!$condition) ? array (
            "orderby" => "id DESC", "limit" => 15
        ) : $condition;
        // 如果启用缓存则通过缓存操作
        if ( $this->enableCache ) {
            $cacheKey = md5 ( $this->tableName . serialize ( $condition ) );
            $result = $this->cache->get ( $cacheKey );
            if ( !$result ) {
                $result = $this->table->fetchRows ( $condition );
                $this->cache->add ( $cacheKey, $result, $this->cacheTime );
                unset ( $condition, $cacheKey );
            }
        }
        else {
            $result = $this->table->fetchRows ( $condition );
        }
        return $result;
    }

    /**
     * 按主键删除
     * @param integer $primaryKeyId
     * @return array
     */
    public function del ( $primaryKeyId ) {
        return $this->table->delete ( $primaryKeyId );
    }

    /**
     * 按条件删除，此处与查询不同。
     * @param array $where
     * @example $where = array('expression' => 'id < :id', 'value' => array('id' => 10));
     * @return bool
     */
    public function delRow ( $where ) {
        return $this->table->deleteRows ( $where );
    }

    /**
     * 按条件统计
     * @param array $condition
     * @example $condition['where'] = array('expression' => 'id < :id', 'value' => array('id' => 10));
     * @return int
     */
    public function count ( $condition ) {
        return $this->table->count ( $condition );
    }

    /**
     * 指定字段取出内容
     * @param string $fields
     * @param $limit
     * @param $offset
     * @param array $where
     * @param bool $enableCache
     * @param string $groupBy
     * @param string $orderBy
     * @return int
     */
    public function countByFieldName ( $fields = '', $limit, $offset, $where = array() , $enableCache = false, $groupBy = '', $orderBy = '') {
        $condition [ 'fields' ] = empty ( $fields ) ? '*' : $fields;
        $condition [ 'fields' ] = ($enableCache) ? "SQL_CACHE " . $condition [ 'fields' ] : $condition [ 'fields' ];
        if ($orderBy) {
            $condition [ 'orderby' ] = $orderBy;
        }

        if ($groupBy) {
            $condition [ 'groupby' ] = $groupBy;
        }
// 		$condition [ 'limit' ] = $limit;
// 		$condition [ 'offset' ] = $offset;
        if ( $where ) {
            $condition [ 'where' ] = $where;
        }
        return $this->table->count ( $condition );
    }

    /**
     * 指定字段取出内容
     * @param string $fields
     * @param $limit
     * @param $offset
     * @param array $where
     * @param bool $enableCache
     * @param string $groupBy
     * @param string $orderBy
     * @return array
     */
    public function getByFieldName ( $fields = '', $limit, $offset, $where = array() , $enableCache = false, $groupBy = '', $orderBy = '') {
        $condition [ 'fields' ] = empty ( $fields ) ? '*' : $fields;
        $condition [ 'fields' ] = ($enableCache) ? "SQL_CACHE " . $condition [ 'fields' ] : $condition [ 'fields' ];
        $condition [ 'orderby' ] = ($orderBy) ? $orderBy : "id DESC";
        if ($groupBy) {
            $condition [ 'groupby' ] = $groupBy;
        }
        $condition [ 'limit' ] = $limit;
        $condition [ 'offset' ] = $offset;
        if ( $where ) {
            $condition [ 'where' ] = $where;
        }
        return $this->getRow ( $condition );
    }

    /**
     * 根据字段内容取出相关得另一个字段得数据
     * @param string $value
     * @param string $field = 'id'
     * @param string $returnField = 'username'
     * @param int $limit = 1
     * @param int $offset
     * @param bool $enableCache
     * @return array
     */
    public function getValueByField ( $value, $field = 'id', $returnField = 'username', $limit = 1, $offset = null, $enableCache = false ) {
        $queryField = $offset = '';
        $queryField = ($enableCache) ? "SQL_CACHE " . $field : $field;
        $condition = array (
            "fields" => $returnField, "where" => array (
                "expression" => "$field = :$field", "value" => array (
                    $field => $value
                )
            ), "limit" => $limit
        );

        if ( $offset ) {
            $condition [ "offset" ] = $offset;
        }

        $row = $this->getRow ( $condition );

        if ( $limit == 1 ) {
            if ( $returnField == '*' || strstr ( $returnField, ',' ) ) {
                return count ( $row ) ? $row [ 0 ] : null;
            }
            else {
                return count ( $row ) ? $row [ 0 ] [ $returnField ] : 0;
            }
        }
        else {
            return $row;
        }
    }

    /**
     * 根据用户序号取出用户名称
     * @param int $Id
     * @return string
     */
    public function getUserNameById ( $Id ) {
        return $this->getValueByField ( $Id );
    }

    /**
     * 根据手机号码取出用户序号
     * @param string $mobile
     * @return int
     */
    public function getIdByMobile ( $mobile ) {
        return $this->getValueByField ( $mobile, "mobile", "id" );
    }
}
