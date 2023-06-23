# Using Puppet, create a manifest that kills a process named killmenow.
# Using exec resource type

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
