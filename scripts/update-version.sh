#!/bin/bash
version=$(date +"%y.%m.%d.%H.%M")
echo -n "$version" > "$(dirname "$0")/../VERSION"
echo "Version updated to: $version"