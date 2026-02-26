#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

locale=$2

if [[ "$locale" == "ru" ]]; then
  files_txt="${script_dir}/../common/files/desk_cyrillic.txt"
else
  files_txt="${script_dir}/../common/files/desk_latin.txt"
fi

# Extract files using 7za
# Password priority: 1. Argument $3, 2. Env Var $SWORCERY_PASSWORD
PASS=${3:-${SWORCERY_PASSWORD}}

if [ -z "$PASS" ]; then
  echo "Error: SWORCERY_PASSWORD not set."
  echo "Please set it via: export SWORCERY_PASSWORD=your_password"
  echo "Or pass it as the 3rd argument: ./unpack.sh <res_dir> <locale> <password>"
  exit 1
fi

7za x -aoa "${res_dir}/sworcery.dat" -i@"$files_txt" -o"${res_dir}" -p"${PASS}"
