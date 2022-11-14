#!/bin/bash

function case_1 {
    # Put demo code here
}

function show_menu {
    echo "0 - exit"
    echo "1 - all"  # TODO: let it 1
    echo "2 - case_1"
}

function run_demo_pack {
    KEY=$1

    case $KEY in
        1)
            # Put here all cases calls
            case_1
            ;;
        2)
            case_1
            ;;
    esac
}

n=1
while [ $n != 0 ]
do
    show_menu
    read -p "Input n: " n
    if [ $n != 0 ]; then
        run_demo_pack $n
        echo "press Enter to continue"
        read
    fi
done
