#!/usr/bin/bash
#
# set Offical

# make pretty looking messages (thanks Carlos)

function print_info () {
    echo -e "\x1B[01;34m[*]\x1B[0m $1"
}

function set_offical() {
    current_dir=$(pwd)
    proj_name="Toolbox_GUI"
    proj_dir="$current_dir/$proj_name/"

    wait_del_filename=('config.ini' 'config/env_myself.py' 'onefox' 'install.sh' 'setoffical.sh')
    wait_mv_filename=('README-EN.md'  'README.md' 'requirements.txt')
    
    for f in "${wait_del_filename[@]}"; do
        rm -rf "$proj_dir$f"
        print_info "rm -rf $proj_dir$f"

    done

    for f in "${wait_mv_filename[@]}"; do
	    mv "$proj_dir$f" "./"
	    print_info "mv $proj_dir$f => ./$f"
    done

}

set_offical
