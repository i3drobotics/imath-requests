#!/bin/bash

# exit on command failure
set -e

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

VERSION=$(cat $SCRIPT_PATH/../version.template)
VERSION=${VERSION//$'\n'/} # Remove newlines.
VERSION=${VERSION//$'\r'/} # Remove carriage returns.

# read issue string from file (issues.md should have been generated in workflow step)
ISSUES=$(cat $SCRIPT_PATH/../issues.md)
# TODO format issues string

cd $SCRIPT_PATH/../
echo "# iMATH Requests $VERSION" > release.md
echo "## Install" >> release.md
echo "Install the package using pip:" >> release.md
echo "\`\`\`" >> release.md
echo "python -m pip install imath-requests" >> release.md
echo "\`\`\`" >> release.md
echo "## Changes" >> release.md
echo "$ISSUES" >> release.md