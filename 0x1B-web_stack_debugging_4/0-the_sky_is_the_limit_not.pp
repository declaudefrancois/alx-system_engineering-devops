# Increase the limit of concurrent requests.
exec { 'Increase the open files number limit of nginx processes':
  command => '/bin/sed "s/^ULIMIT.*/ULIMIT=\"-n 4086\"/" -i /etc/default/nginx'
}-> exec { 'Restart nginx':
  command => '/usr/sbin/service nginx restart'
}
