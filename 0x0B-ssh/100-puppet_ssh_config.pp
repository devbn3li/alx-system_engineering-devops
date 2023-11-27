#Create a File in /tmp
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "# This is the ssh client system-wide configuration file.

Include /etc/ssh/ssh_config.d/*.conf

Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
",
  mode    => '0644',
}
