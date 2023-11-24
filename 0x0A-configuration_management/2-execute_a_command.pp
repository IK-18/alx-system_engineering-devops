#  kills a process named killmenow

exec { 'pkill':
  command  => 'pkill killmeniow',
  provider => 'shell',
}
