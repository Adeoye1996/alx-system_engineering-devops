# fix nginx to accept and serve

exec { 'increase nginx open files limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
