# Install & setup Nginx web server using puppet
package { 'nginx':
  ensure  => installed
}


$content = "server {
              listen 80 default;
              server_name _;
              add_header X-Served-By ${hostname};
	      root /var/www/html/;
              location / {
                try_files \$uri \$uri/ \$uri.html =404;
              }
           }"

file{'/var/www/html/index.html':
  ensure  => present,
  content => '<!DOCTYPE html><html><head></head><body><h1>Hello world !</h1></body></html>',
  require => Package['nginx'],
} -> file { '/etc/nginx/sites-available/default':
  content => $content,
} -> exec {'Restart nginx':
  command => '/usr/sbin/service nginx restart',
  user    => root,
}
