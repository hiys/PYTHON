import tarfile

tar = tarfile.open('/tmp/aaa.tar.gz', 'w:gz')
tar.add('/etc/passwd')
tar.add('/etc/security')
tar.close()
# tar tvzf /tmp/aaa.tar.gz
