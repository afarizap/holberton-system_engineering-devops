# set up your client SSH configuration file so that you can connect to a server
# without typing a password.
File_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'BachMode yes',
}
File_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
