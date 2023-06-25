# using Puppet to make changes to our configuration file
# SSH client configuration must be configured to use the private
# key ~/.ssh/school
# SSH client configuration must be configured to refuse to authenticate
# using a password
# Resource type used = file_line (manage specific lines in ssh client
# configuration file

include stdlib

file_line { 'No authentication with password':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Specify identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}
