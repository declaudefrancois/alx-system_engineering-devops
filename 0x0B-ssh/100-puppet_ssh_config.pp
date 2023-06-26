# setup a client configuration to file sot that if connects to a server without typing a password.
# the client will connect using the private key in ~/.ssh/school

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "HOST *\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school\n"
}
