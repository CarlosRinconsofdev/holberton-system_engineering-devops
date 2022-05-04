# This Puppet manifest is about how to kills a process named killmenow.

exec { 'killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
