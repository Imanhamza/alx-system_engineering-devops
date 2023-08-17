# Change the OS configuration for Halbrton user
exec { 'holberton':
  command => 'sed -i -e "/holberton hard/s/5/50000/" -e "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}
