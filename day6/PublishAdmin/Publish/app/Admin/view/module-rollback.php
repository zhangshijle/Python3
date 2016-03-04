<legend>回滚模块<?php echo $this->data['name'];?></legend>

<form class="form-horizontal" method="post" action="{url("Module","Rollback",array('name'=>$this->data['name'], 'do'=>'run'))}">
    <fieldset>

        <div class="control-group">
            <label for="version_type" class="control-label">回滚版本：</label>
            <div class="col-lg-10">
                <input type="radio" name="version_type" id="version_type1"
                       value="1" checked
                       onclick="javascript:document.getElementById('version_list').style.display='none';"> 上一个版本
                <input type="radio" name="version_type" id="version_type2" value="2" onclick="javascript:document.getElementById('version_list').style.display='';"> 其他版本
            </div>
        </div>

        <div class="control-group" id="version_list" style="display:none">
            <label for="version" class="control-label">选择相应版本：</label>
            <div class="col-lg-10">
                <select class="form-control" name="version" id="select">
                    <?php
                    if($this->data['module_version']){
                        foreach( $this->data['module_version'] as $v){
                            echo "<option>".substr(strrchr($v, "/"), 1)."</option>";
                        }
                    }else{
                        echo "<option value=''>不存在历史版本</option>";
                    }
                    ?>
                </select>
            </div>
        </div>



        <div class="form-group">
            <div class="offset2">
                <button type="submit" class="btn btn-primary">执行回滚</button>
            </div>
        </div>

    </fieldset>
</form>