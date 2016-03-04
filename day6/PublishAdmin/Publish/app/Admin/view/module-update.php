
<legend>更新模块<?php echo $this->data['name'];?></legend>
<div class="bigUpload">
    <div class="bigUploadContainer">
        <form action="bigUpload.php?action=post-unsupported" method="post" enctype="multipart/form-data" id="bigUploadForm">
            <input type="file" id="bigUploadFile" name="bigUploadFile" />
            <input type="button" class="bigUploadButton" value="开始上传" id="bigUploadSubmit" onclick="upload()" />
            <input type="button" class="bigUploadButton bigUploadAbort" value="取消上传" onclick="abort()" />
        </form>
        <div id="bigUploadProgressBarContainer">
            <div id="bigUploadProgressBarFilled">
            </div>
        </div>
        <div id="bigUploadTimeRemaining"></div>
        <div id="bigUploadResponse"></div>
    </div>
</div>

<script src="style/js/bigUpload.js" type="text/javascript"></script>
<script type="text/javascript">
    bigUpload = new bigUpload();
    bigUpload.settings.scriptPathParams = '&moduleName=<?php echo $this->data['name'];?>';
    bigUpload.settings.redirectUrl = '{url("Module","Update",array("name"=>$this->data["name"], "do"=>"confirmUpdate"))}';
    function upload() {
        bigUpload.fire();
    }
    function abort() {
        bigUpload.abortFileUpload();
    }
</script>