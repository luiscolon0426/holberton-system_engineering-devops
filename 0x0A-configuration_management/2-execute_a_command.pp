# Using puppet, create a manifest that
# kills a proccess named killmenow

exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
