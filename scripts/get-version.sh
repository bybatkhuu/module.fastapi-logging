#!/bin/bash
set -euo pipefail

## --- Base --- ##
# Getting path of this script file:
_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
_PROJECT_DIR="$(cd "${_SCRIPT_DIR}/.." >/dev/null 2>&1 && pwd)"
cd "${_PROJECT_DIR}" || exit 2

# Loading .env file:
if [ -f ".env" ]; then
	# shellcheck disable=SC1091
	source .env
fi
## --- Base --- ##


## --- Variables --- ##
# Load from envrionment variables:
VERSION_FILE="${VERSION_FILE:-my_template/__version__.py}"
## --- Variables --- ##


if [ -n "${VERSION_FILE}" ] && [ -f "${VERSION_FILE}" ]; then
	_current_version=$(< "${VERSION_FILE}" grep "__version__ = " | awk -F' = ' '{print $2}' | tr -d '"') || exit 2
else
	_current_version="0.0.0"
fi

echo "${_current_version}"
