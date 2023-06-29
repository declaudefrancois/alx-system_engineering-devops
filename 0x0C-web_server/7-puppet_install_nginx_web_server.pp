# Install & setup Nginx web server usign puppet
package { 'nginx':
  ensure  => installed
}

file { '/etc/nginx/sites-available/default':
  content => "server {\n\tlisten 80 default;\n\trewrite ^/redirect_me\\/?$ https://www.youtube.com permanent;\n\tlocation = / {\n\t\treturn 200 \"Hello World!\\n\";\n\t}\n}",
  require => Package['nginx']
}

exec {'Restart nginx':
  command => '/usr/sbin/service nginx restart',
  user    => root,
  require => Package['nginx']
}

exec {'Reload nginx':
  command => '/usr/sbin/nginx -s reload',
  user    => root,
  require => Package['nginx']
}
