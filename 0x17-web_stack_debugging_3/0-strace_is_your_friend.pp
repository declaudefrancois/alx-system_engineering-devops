# Fix the broken web server
exec { 'Fix typos':
  command  => "/bin/sed 's/class-wp-locale.phpp/class-wp-locale.php/' -i /var/www/html/wp-settings.php"
}
