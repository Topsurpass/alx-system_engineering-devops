# This enables the user holberton to login and open files without error
# This is done by searching for the user and adjusting the domain's item
#  and item's value in the /etc/security/limits.conf file

exec { 'Increase the hard file limit for user holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'Increase the soft file limit for user holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
