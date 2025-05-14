#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/.venv/bin/activate"

countdown -t "Cantarell, Light" -p 100 -f

