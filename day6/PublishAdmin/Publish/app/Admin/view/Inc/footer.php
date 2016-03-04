<hr>
<footer><p>&copy; 高校邦科技有限公司 2016</p></footer>
</div>
<?php
if(isset($this->data["footer_js"]) && strlen($this->data["footer_js"])){
    echo '<script src="'. $baseURL .'style/js/jquery-1.7.2.min.js?v=1" type="text/javascript"></script>';
    echo '<script src="'. $baseURL .'style/js/bootstrap-ie.js?v=1" type="text/javascript"></script>';
    echo $this->data["footer_js"];
}
?>
<?php if ($this->data['HtmlEditor']){?>
<script src="{$this->data['HtmlEditor']}?v=1" type="text/javascript"></script>
<?php }?>
</body>
</html>
