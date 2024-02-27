<?php
    if (!isset($_COOKIE['cl4y'])) {
        setcookie('cl4y',md5(rand(0,1000)));
    }
        header("Content-Security-Policy: default-src 'self';");
?>
<!DOCTYPE html>
<html>
<head>
    <title>CSP Test</title>
</head>
<body>
<h2>CSP-safe</h2>
<?php
    if (isset($_GET['cl4y'])) {
        echo "Your GET content:".@$_GET['cl4y'];
    }//
?>
</body>
