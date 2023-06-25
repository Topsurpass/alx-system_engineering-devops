# using Puppet to make changes to our configuration file
# SSH client configuration must be configured to use the private
# key ~/.ssh/school
# SSH client configuration must be configured to refuse to authenticate
# using a password
# Resource type used = file

file {'ssh_configuration':
  ensure  => 'file',
  path    => '/home/vagrant/.ssh/config',
  content => 'Host 54.237.54.19
	PasswordAuthentication no
	IdentityFile ~/.ssh/school'
}
