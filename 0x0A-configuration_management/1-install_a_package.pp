# Installs Flask, in /tmp version 2.1.0

#package { 'puppet-lint':
#  ensure   => '2.5.0',
#  provider => 'gem',
#  source   => 'http://rubygems.org',
#}


exec {'flask_install':
  command  => 'pip3 install Flask==2.1.0',
  provider => shell,
  #path    => ['/usr/bin', '/bin'],
}
