# kills a process named killmenow.
exec { 'kills killmenow.':
  command => 'killall killmenow',
  path    => '/usr/bin'
}

