#!/bin/bash

# Get the directory of the script
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
# Get the project root
project_root=$(cd "${script_dir}/../.." && pwd)

# Validate the number of arguments
if [ $# -lt 1 ]; then
  echo "Usage: $0 <sworcery.dat_path> [locale]"
  exit 1
fi

# Get the sworcery.dat path from the argument
sworcery_dat_path=$1

# Validate if the sworcery.dat file exists
if [ ! -f "$sworcery_dat_path" ]; then
  echo "The sworcery.dat file does not exist at the specified path: $sworcery_dat_path"
  exit 1
fi

# Set locale argument
locale=${2:-"es"}
# Set password argument
password=${3:-$SWORCERY_PASSWORD}

if [ -z "$password" ]; then
  echo "Error: SWORCERY_PASSWORD not set."
  echo "Please set it via: export SWORCERY_PASSWORD=your_password"
  echo "Or pass it as the 3rd argument: ./build.sh <dat_path> <locale> <password>"
  exit 1
fi

source "${script_dir}/../common/validate_locale.sh"
validate_locale "$locale"

# Set the res dir based on the project root
mkdir -p "${project_root}/build/steam/$locale"
res_dir=$(cd "${project_root}/build/steam/$locale" && pwd)

# Copy the sworcery.dat file to the res directory
cp "$sworcery_dat_path" "$res_dir"

# Double check if sworcery.dat exists in res_dir
if [ ! -f "${res_dir}/sworcery.dat" ]; then
  echo "Error: Failed to copy sworcery.dat to ${res_dir}"
  exit 1
fi

# Run the unpack.sh script
# "${script_dir}/unpack.sh" "$res_dir" "$locale"

# Run the copy_files.sh script
"${script_dir}/../common/copy_files.sh" "$res_dir" "$locale" "desk"

if [ $? -ne 0 ]; then
  echo "Error: Copy files script failed."
  exit 1
fi

# Run the repack.sh script
"${script_dir}/repack.sh" "$res_dir" "$locale" "$password"

if [ $? -ne 0 ]; then
  echo "Error: Repack .dat failed."
  exit 1
fi


# Run the build-cat.py script
"${script_dir}/build-cat.py" "$res_dir"

if [ $? -ne 0 ]; then
  echo "Error: Copy files script failed."
  exit 1
else
  echo "Localization build completed for locale: $locale"
fi

