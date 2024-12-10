# Utils file with the function to install the certificate for mac only.

import os
import ssl
import subprocess
import sys
import certifi
import stat

STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
             | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
             | stat.S_IROTH |                stat.S_IXOTH )

def install_cert():
    # Get the path to the openssl directory
    openssl_dir, openssl_cafile = os.path.split(ssl.get_default_verify_paths().openssl_cafile)
    print(openssl_dir, openssl_cafile)

    
    # Get the path to the certificate file in ssl
    abspath_to_ssl_certifi = os.path.join(openssl_dir, openssl_cafile)
    print("Abs to ssl certificate file:", abspath_to_ssl_certifi)

    # Get the path to the certificate file
    abspath_to_certifi_cafile = os.path.abspath(certifi.where())
    print("Abs to certifi certificate file:", abspath_to_certifi_cafile)
    
    # remove existing file or link
    print("Removing existing file or link")
    try:
        os.remove(abspath_to_ssl_certifi)
    except FileNotFoundError:
        pass

    # Create a symbolic link to the certifi certificate file
    print("Creating symbolic link to the certifi certificate")
    os.symlink(abspath_to_certifi_cafile, abspath_to_ssl_certifi)

    # Set the permissions of the file
    
    os.chmod(abspath_to_ssl_certifi, STAT_0o775)