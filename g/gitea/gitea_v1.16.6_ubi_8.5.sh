#!/bin/bash -e          
# ----------------------------------------------------------------------------         
#         
# Package       : gitea         
# Version       : v1.16.6         
# Source repo   : https://github.com/go-gitea/gitea         
# Language	  : Go         
# Tested on     : ubi_8.5         
# Travis-Check  : True         
# Script License: Apache License Version 2.0          
# Maintainer    : saurabh-gore         
# Disclaimer: This script has been tested in root mode on given         
# ==========  platform using the mentioned version of the package.         
#             It may not work as expected with newer versions of the         
#             package and/or distribution. In such case, please         
#             contact Maintainer of this script.         
# ---------------------------------------------------------------------------- 
PACKAGE_VERSION=${1:-1.16.6}

# Install docker if not found
if ! [ $(command -v docker) ]; then
	sudo yum install -y docker
fi

# Install git if not found
if ! [ $(command -v git) ]; then
	sudo yum install -y git
fi

git clone https://github.com/go-gitea/gitea && cd gitea

git checkout v$PACKAGE_VERSION

# Use ppc64le supported base images
sed -i 's|techknowlogick/go:1.16-alpine3.13|golang:1.16-alpine3.15|' Dockerfile
sed -i 's|alpine:3.13|alpine:3.15|' Dockerfile

docker build --rm -t gitea:$PACKAGE_VERSION .