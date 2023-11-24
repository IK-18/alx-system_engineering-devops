#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package { ['flask==2.1.0', 'werkzeug==2.1.1']:
  ensure   => 'present',
  provider => 'pip3',
}
