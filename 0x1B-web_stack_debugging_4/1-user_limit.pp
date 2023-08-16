# Increase the user `holberton` open files limit.
$hard = 's/holberton hard nofile .*/holberton hard nofile 4096/'
$soft = 's/holberton soft nofile .*/holberton soft nofile 1024/'
exec {'Increase holberton user open files limit':
  command => "/bin/sed '${hard};${soft}' -i /etc/security/limits.conf"
}
