#  kills a process named killmenow.
exec { 'pkill -SIGKILL killmenow':
  command  => '/usr/bin/pkill -SIGTERM killmenow'
}
