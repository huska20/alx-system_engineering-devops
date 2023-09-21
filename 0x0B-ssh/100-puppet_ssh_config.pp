# Ensure the SSH client configuration directory exists for the ubuntu user
file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Configure SSH to use the private key ~/.ssh/school for the ubuntu user
file_line { 'Configure SSH to use the private key':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/home/ubuntu/.ssh'],
}

# Refuse to authenticate using a password for the ubuntu user
file_line { 'Refuse password authentication':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/home/ubuntu/.ssh'],
}
