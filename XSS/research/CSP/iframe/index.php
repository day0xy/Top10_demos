<!--index.php-->
<!DOCTYPE html>
<html>
<head>
    <title>CSP Test</title>
</head>
<body>
<h2>CSP</h2>
<?php
    if (isset($_GET['cl4y'])) {
        echo "Your GET content:".@$_GET['cl4y'];
    }//
?>
</body>