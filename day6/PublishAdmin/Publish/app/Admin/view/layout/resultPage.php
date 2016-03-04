<?php
// 根据代码替换成中文信息
switch ($this->code)
{
    case '200':
        $this->message = $this->message ? $this->message : '您的操作已成功处理!';
        $msgType = 'alert alert-success';
        break;
    case '403':
        $this->message = $this->message ? $this->message : '对不起，您无权访问该页面!';
        $msgType = 'alert alert-block';
        break;
    case '404':
        $this->message = $this->message ? $this->message : '对不起，未找到该页面!';
        $msgType = 'alert alert-block';
        break;
    case '405':
        $this->message = $this->message ? $this->message : '对不起，操作失败，请稍后重试!';
        $msgType = 'alert alert-block';
        break;
    case '406':
        $this->message = $this->message ? $this->message : '您提交的参数在验证过程中出错，请您检查错误后重新提交数据!';
        $msgType = 'alert alert-error';
        break;
    case '407':
        $this->message = $this->message ? $this->message : '您的输入中含有无效的内容，请您检查您输入的内容后重试!';
        $msgType = 'alert alert-error';
        break;
    case '1000':
        $this->message = $this->message ? $this->message : '您当前操作的数据为系统的重要组建，该组件暂不可删除!';
        $msgType = 'alert alert-block';
        break;
    case '1001':
        $this->message = $this->message ? $this->message : '您输入的模型标识，已有记录，请重新填写。';
        $msgType = 'alert alert-block';
        break;
    case '1002':
        $this->message = $this->message ? $this->message : '该模型未配置数据字典，所以不能取出数据。';
        $msgType = 'alert alert-block';
        break;
    case '510':
        $msgType = 'alert alert-block';
        break;
    default:
        $msgType = 'alert alert-block';
}
if(empty($this->message))
{
    $this->message = '';//'提示信息';
}
?>
{include 'Inc/header'}
{include "Inc/topmenu"}
<div class="container-fluid">
    <div class="row-fluid">
        <div class="span2">
            {include 'Inc/leftmenu'}
        </div>
        <div class="span10">
            <div class="page-header">
                <h4><?php echo $this->data['title'];?> <small>操作提示</small></h4>
            </div>
            <div class="{$msgType}">
                <button type="button" class="close" data-dismiss="alert">×</button>
                <h4>提示信息!</h4>
                <?php echo $this->message;?>
                <?php
                if (isset($this->data['error_messages']) && is_array($this->data['error_messages']))
                {
                    foreach($this->data['error_messages'] as $dtd)
                    {
                        foreach($dtd as $msg)
                        {
                            echo "<p>$msg</p>";
                        }
                    }
                }
                ?>
            </div>
        </div><!--/span-->
    </div><!--/row-->
    {include 'Inc/footer'}