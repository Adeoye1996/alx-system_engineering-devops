# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define the Nginx configuration file
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World',
}

# Add redirection to Nginx configuration
file_line { 'nginx_redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'listen 80 default_server;',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
