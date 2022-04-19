# Installs puppet-lint, in /tmp version 2.5.0

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  source   => 'http://rubygems.org',
}
