#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
exec { 'install_flask':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => 'pip3 show flask | grep -q "Version: 2.1.0"',
}
