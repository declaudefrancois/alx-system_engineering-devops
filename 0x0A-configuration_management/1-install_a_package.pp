# Ensure pip3 is installed.
package { 'python3-pip':
  ensure  => 'installed',
}

# Install flask version 2.1.0 using pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip']
}
