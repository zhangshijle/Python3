{include 'Inc/header'}
{include "Inc/topmenu"}
<div class="container-fluid">
    <div class="row-fluid">
        <div class="span2">
{include 'Inc/leftmenu'}
        </div>
        <div class="span10">
{include $this->templateDir . $this->template . '.php'}
        </div>
    </div>
{include 'Inc/footer'}