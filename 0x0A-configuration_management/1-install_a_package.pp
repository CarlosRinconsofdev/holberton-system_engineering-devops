# This Puppet manifest is about how to install flask from pip3 using puppet

package {'flask':
ensure   => '2.1.0',
provider => 'pip3',
}
