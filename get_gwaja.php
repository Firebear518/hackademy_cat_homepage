<?php
    echo "아까 저장한 쿠키, 확인해보겠습니다. <br>";
    $race_cookie = $_COOKIE['race'];
    $job = $_COOKIE['user_status'];

    echo "너의 인종: $race_cookie";
    echo "<br>";
    echo "너의 직업: $job";
?>