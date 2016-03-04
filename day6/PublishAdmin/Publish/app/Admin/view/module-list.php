

<legend>模块列表</legend>
<table class="table table-striped table-hover ">
    <thead>
    <tr>
        <th>模块名称</th>
        <th>部署路径</th>
        <th>ip</th>
        <th>配置详情</th>
        <th>更新信息</th>
        <th>操作</th>
    </tr>
    </thead>
    <tbody>
    <?php foreach($this->data['list'] as $key=>$val):
        if(empty($val)) continue;
        ?>
    <tr>
        <td><?php echo $key;?></td>
        <td><?php echo $val['path'];unset($val['path']);?></td>
        <td><?php echo $val['ip'];unset($val['ip']);?></td>
        <td><?php
            if(isset($val['is_compress'])){
                echo "is_compress:".($val['is_compress'] ? "True" : "False")."<br />";
                unset($val['is_compress']);
            }
            foreach($val as $k=>$v){
                echo "$k:$v<br/>";
            }
            ?></td>
        <td></td>
        <td><div class="bs-component" style="margin-bottom: 40px;">

                <a class="label label-warning" href="{url("Module","Edit",array('name'=>$key))}">编辑</a>
                <a class="label label-info" href="{url("Module","Update",array('name'=>$key,'do'=>'updateType'))}">更新</a>
                <a class="label label-success"  href="{url("Module","Backup",array('name'=>$key))}">备份</a>
                <a class="label label-danger" href="{url("Module","Rollback",array('name'=>$key))}">回滚</a>

            </div></td>
    </tr>
    <?php endforeach;?>

    </tbody>
</table>