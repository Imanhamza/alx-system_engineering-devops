# Fixing Ngnix under pressure
exec { 'fix Nginx':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
  provider => shell,
}
