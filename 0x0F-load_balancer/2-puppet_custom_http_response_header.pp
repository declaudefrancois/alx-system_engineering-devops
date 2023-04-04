# Nginx custom HTTP header with Puppet.

# Install nginx
exec { 'Install nginx':
  command => 'apt-get update && apt-get install -y nginx',
  path    => '/usr/bin' 
}


# Create the html pages to serve.
exec { 'Create hmtl pages':
  command => 'mkdir -p /var/www/hello_world && echo "Hello World!" > /var/www/hello_world/index.html',
  path    => '/usr/bin'
}

# Configure nginx
exec { 'Configure nginx':
  command => 'echo "server {\n\tlisten 80 default_server;\n\tadd_header X-Served-By $HOSTNAME;\n\tlocation = / {\n\t\tindex index.html;\n\t}\n}" > /etc/nginx/sites-enabled/default',
  path    => '/usr/bin'
}

# restart nginx
exec { 'REstart nginx':
  command => 'systemctl restart nginx',
  path    => '/usr/bin'
}
