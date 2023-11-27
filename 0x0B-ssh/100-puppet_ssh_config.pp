#!/usr/bin/env bash
# Using puppet to modify config file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "

	#SSH client config
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	"
}
