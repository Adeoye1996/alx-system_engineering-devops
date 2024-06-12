exec { 'modify os security config':
  command => '/usr/bin/sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => ['/usr/bin/env', '/bin', '/usr/bin', '/usr/sbin'],
}
