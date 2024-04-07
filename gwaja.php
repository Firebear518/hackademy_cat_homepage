<?php
    ob_start();
    echo "너에게 쿠키를 저장하겠습니다.";
    setcookie("user_status", "student", time()+3600, "/");
    setcookie("race", "Asian", time()+3600, "/");
?>