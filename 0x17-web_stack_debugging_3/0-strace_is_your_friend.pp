# Fix the wrong file name in /var/www/html/wp-settings.php
# Rename the file from .phpp to .php

exec { 'fix typo file name in config file':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
