# This Puppet manifest changes the OS configuration so that it is possible
# to login with the user 'holberton' and open a file without any error message.

exec { 'OS security config':
  command => '/bin/sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => ['/usr/bin/env', '/bin', '/usr/bin', '/usr/sbin'],
}
