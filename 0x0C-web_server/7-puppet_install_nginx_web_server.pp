#Configuring my webserver(Ngnix) using puppet

exec {'install':
  provider => shell,
  command  => "sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo ufw allow 'Nginx HTTP'"
}

exec {'html content':
  provider => shell,
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;'
}

file_line { 'nginx_redirect':
  ensure => present,
  line   => 'rewrite ^/redirect_me https://www.youtube.com/ permanent;',
  match  => 'listen 80 default_server',
  after  => 'match',
  path   => '/etc/nginx/sites-available/default',
}
exec {'restart webserver':
  provider => shell,
  command  => 'sudo service nginx start'
}
