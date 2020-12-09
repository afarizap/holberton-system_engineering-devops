# set up your client SSH configuration file so that you can connect to a server
# without typing a password.
exec { 'Turn off passwd auth':
    path => '/usr/bin',
    content => 'echo "BachMode yes" >> /etc/ssh/ssh_config',
}
exec { 'Declare identity file':
  path => '/usr/bin',
  content => 'echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
}