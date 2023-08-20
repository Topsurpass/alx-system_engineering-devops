# Optimize nginx server by increasing the amount of traffic it can handle
# This is required for application with high load or traffic
# This is achieved by adjusting the /etc/default/nginx configuration file
# and increasing the ULIMIT of the file

#search for 15 and replace with 4096
exec { 'Increase ULIMIT':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'Restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
