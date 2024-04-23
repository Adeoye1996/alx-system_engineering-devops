# install nginx, listen on port 80
# GET with curl return "Hello World"
# redirection must a 301 Moved permanently

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define the Nginx configuration file
file { '/var/www/html/index.html':
  content => 'Hello World',
  path    => '/var/www/html/index.html'
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
