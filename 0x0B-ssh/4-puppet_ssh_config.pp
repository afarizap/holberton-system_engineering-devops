file { 'Turn off passwd auth':
    path => '/etc/ssh/ssh_config',
    content => 'BachMode yes',
}
file { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  content => '~/.ssh/holberton',
}