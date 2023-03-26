# Client configuration file (w/ Puppet)
exec { 'Turn off passwd auth':
  command => 'echo "Host *\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
exec { 'Declare identity file':
  command => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}

