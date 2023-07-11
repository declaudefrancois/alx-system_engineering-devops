# Install & setup Nginx web server using puppet
package { 'nginx':
  ensure  => installed
}

$content = "server {
              listen 80 default;
              server_name _;
              add_header X-Served-By ${hostname};

              rewrite ^/redirect_me\\/?$ https://www.youtube.com permanent;

              location = / {
                return 200 \"Hello World!\\n\";
              }

              location / {
                return 404 \"Ceci n\'est pas une page\\n\\n\";
              }
           }"

file { '/etc/nginx/sites-available/default':
  content => $content,
  require => Package['nginx']
} -> exec {'Restart nginx':
  command => '/usr/sbin/service nginx restart',
  user    => root,
}
