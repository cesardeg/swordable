#!/bin/bash

# Get the directory of the script
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# Set the res_dir argument to script_dir if not provided
res_dir=${1:-"$script_dir"}

locale=$2

if [[ "$locale" == "ru" ]]; then
  files_txt="${script_dir}/../common/files/desk_cyrillic.txt"
else
  files_txt="${script_dir}/../common/files/desk_latin.txt"
fi

# Copy listfile locally to avoid path issues with 7za on Windows
listfile_name=$(basename "${files_txt}")
cp "${files_txt}" "${res_dir}/${listfile_name}"

# Update the sworcery.dat file using 7za
# Password priority: 1. Argument $3, 2. Env Var $SWORCERY_PASSWORD
PASS=${3:-${SWORCERY_PASSWORD}}

if [ -z "$PASS" ]; then
  echo "Error: SWORCERY_PASSWORD not set."
  echo "Please set it via: export SWORCERY_PASSWORD=your_password"
  echo "Or pass it as the 3rd argument: ./repack.sh <res_dir> <locale> <password>"
  exit 1
fi

(cd "${res_dir}" && 7za u sworcery.dat @"${listfile_name}" -p"${PASS}")
