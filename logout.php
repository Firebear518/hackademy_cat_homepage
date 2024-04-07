<?php
    // delete cookie
    ob_start();
    setcookie('user', '', time() - 3600);

    // Redirect to the login page
    header('Location: index.php');
    exit();
?>