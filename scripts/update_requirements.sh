#!/bin/bash

set -e

cd "$(git rev-parse --show-toplevel)"

source ./scripts/python_cmd.sh

"$PYTHON" -m pip install --upgrade pip

if [ ! -f "./requirements.txt" ]; then
    echo "requirements.txt not found in project root!"
    exit 1
fi

"$PYTHON" -m pip install --upgrade -r ./requirements.txt

"$PYTHON" -m pip freeze > ../requirements.txt
