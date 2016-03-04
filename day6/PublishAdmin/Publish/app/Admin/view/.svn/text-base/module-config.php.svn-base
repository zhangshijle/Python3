
<legend>系统配置</legend>
<form class="form-horizontal" method="post">
    <fieldset>

        <div class="control-group">
            <label for="upload_path" class="control-label">上传目录：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" value="<?php if(isset($this->data['configs']['path']['upload_path'])) echo $this->data['configs']['path']['upload_path'];?>" id="upload_path" name="data[upload_path]" placeholder="upload_path">（必填）
            </div>
        </div>

        <div class="control-group">
            <label for="backup_path" class="control-label">备份目录：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" value="<?php if(isset($this->data['configs']['path']['backup_path'])) echo $this->data['configs']['path']['backup_path'];?>" id="backup_path" name="data[backup_path]" placeholder="backup_path">(必填)
            </div>
        </div>
        <div class="control-group">
            <label for="rollback_path" class="control-label">回滚目录：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" value="<?php if(isset($this->data['configs']['path']['rollback_path'])) echo $this->data['configs']['path']['rollback_path'];?>" id="rollback_path" name="data[rollback_path]" placeholder="rollback_path">(必填)
            </div>
        </div>


        <div class="form-group">
            <div class="offset2">
                <button type="submit" class="btn btn-primary">提交</button>
            </div>
        </div>


    </fieldset>
</form>