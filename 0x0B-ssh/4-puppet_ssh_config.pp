# set up your client SSH configuration file so that you can connect to a server
# without typing a password.
file { 'Turn off passwd auth and Declare identity file':
    path => '/etc/ssh/ssh_config',
    content => 'BachMode yes\nIdentityFile ~/.ssh/holberton',
}
