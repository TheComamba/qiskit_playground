#!/bin/bash

set -e

cd "$(git rev-parse --show-toplevel)"

source ./scripts/python_cmd.sh

"$PYTHON" $1
