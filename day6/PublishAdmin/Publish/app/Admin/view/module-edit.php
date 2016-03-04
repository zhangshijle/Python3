
<legend>编辑模块</legend>
<form class="form-horizontal" method="post">
    <fieldset>

        <div class="control-group">
            <label for="name" class="control-label">模块名称：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="name" name="name" placeholder="name" value="<?php echo $this->data['name'];?>">（必填）
            </div>
        </div>
        <div class="control-group">
            <label for="select" class="control-label">模块类型：</label>
            <div class="col-lg-10">
                <select class="form-control" name="data[type]" id="select">
                    <?php
                        foreach($this->data['moduleType'] as $val){
                            echo "<option ".($this->data['data']['type']==$val ? 'selected' : '').">$val</option>";
                        }
                    ?>
                </select>
            </div>
        </div>

        <div class="control-group">
            <label for="path" class="control-label">部署路径：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="path" name="data[path]" placeholder="path" value="<?php if(isset($this->data['data']['path'])) echo $this->data['data']['path'];?>">（必填）
            </div>
        </div>

        <div class="control-group">
            <label for="ip" class="control-label">服务器IP：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="ip" name="data[ip]" placeholder="ip" value="<?php if(isset($this->data['data']['ip'])) echo $this->data['data']['ip'];?>">(必填 多个ip 使用竖线（|）分割 ip = 1.1.1.1|2.2.2.2)
            </div>
        </div>

        <div class="control-group">
            <label for="port" class="control-label">服务器端口：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="port" name="data[port]" placeholder="port" value="<?php if(isset($this->data['data']['port'])) echo $this->data['data']['port'];?>">(必填)
            </div>
        </div>

        <div class="control-group">
            <label for="tomcat_path" class="control-label">tomcat路径：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="tomcat_path" name="data[tomcat_path]" placeholder="tomcat_path" value="<?php if(isset($this->data['data']['tomcat_path'])) echo $this->data['data']['tomcat_path'];?>">
            </div>
        </div>

        <div class="control-group">
            <label for="user" class="control-label">ssh用户名：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="user" name="data[user]" placeholder="user" value="<?php if(isset($this->data['data']['user'])) echo $this->data['data']['user'];?>">（用户名 多个用逗号（,）分割）
            </div>
        </div>

        <div class="control-group">
            <label for="password" class="control-label">ssh密码：</label>
            <div class="col-lg-10">
                <input type="text" class="form-control" id="password" name="data[password]" placeholder="password" value="<?php if(isset($this->data['data']['password'])) echo $this->data['data']['password'];?>">（密码 多个用逗号（,）分割）
            </div>
        </div>

        <div class="control-group">
            <label for="is_compress2" class="control-label">上传文件是否是压缩包：</label>
            <div class="col-lg-10">
                <input type="radio" name="data[is_compress]" id="is_compress1" value="True" <?php if(isset($this->data['data']['is_compress']) && $this->data['data']['is_compress']){echo "checked";}?>> 是
                <input type="radio" name="data[is_compress]" id="is_compress2" <?php if(!isset($this->data['data']['is_compress']) || !$this->data['data']['is_compress']){echo "checked";}?>> 否
            </div>
        </div>
        <div class="control-group">
            <label for="is_compress2" class="control-label">更多参数：</label>
            <div class="col-lg-10">
                <table>
                    <tr><td>
                            <textarea name="data_more" class="form-control" rows="8" placeholder="k1=v1">
                                <?php
                                $unset_data = array('name', 'type', 'path', 'ip', 'port', 'tomcat_path', 'user','password', 'is_compress');
                                foreach($unset_data as $k){
                                    if(isset($this->data['data'][$k])) unset($this->data['data'][$k]);
                                }

                                foreach($this->data['data'] as $k=>$v){
                                    echo "$k=$v\n";
                                }

                                ?>
                            </textarea>
                        </td><td>
                            (内容为k/v格式，以换行分割 如下:<br>
                            k1=v1<br>
                            k2=v2
                            <br>)
                        </td></tr></table>
            </div>
        </div>

        <div class="form-group">
            <div class="offset2">
                <button class="btn btn-default">取消</button>
                <button type="submit" class="btn btn-primary">提交</button>
            </div>
        </div>
    </fieldset>
</form>