# Install & setup Nginx web server usign puppet
package { 'nginx',
  ensure  => installed
}

$content = "server {
       		listen 80 default;

		rewrite ^/redirect_me$ https://www.youtube.com permanent;
		location = \ {
			return 200 "Hello World!";
		}
	}
        "

file { '/etc/nginx/sites-available/default':
  content => $content,
  require => Package['nginx']
}

exec {'Reload nginx'
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}
