# Using Puppet, install flask from pip3
# Using package resource type

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
