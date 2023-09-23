# A Puppet Script to install flask from pip3 and ensure its version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
