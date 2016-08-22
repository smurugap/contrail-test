#!/bin/bash


SCREEN_NAME="sol_traffic"
TEST_MODE="feature_ping_only"
COMPUTE="dpdk"

screen -d -m -S $SCREEN_NAME

screen -S $SCREEN_NAME -X screen -t "create_del"
screen -S $SCREEN_NAME -p "create_del" -X stuff "source /root/sol_test/bin/activate && sh -x new5_create_delete_tenants.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "vn_flags"
screen -S $SCREEN_NAME -p "vn_flags"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_vn_flags.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "fat"
screen -S $SCREEN_NAME -p "fat"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_fat.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "si1ip4"
screen -S $SCREEN_NAME -p "si1ip4"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_si.v1.ipv4.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "si1ip6"
screen -S $SCREEN_NAME -p "si1ip6"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_si.v1.ipv6.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "si2ip4"
screen -S $SCREEN_NAME -p "si2ip4"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_si.v2.ipv4.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "si2ip6"
screen -S $SCREEN_NAME -p "si2ip6"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_si.v2.ipv6.sh $TEST_MODE $COMPUTE\n"

screen -S $SCREEN_NAME -X screen -t "mirr"
screen -S $SCREEN_NAME -p "mirr"   -X stuff "source /root/sol_test/bin/activate && sh -x new5_mirror.sh $TEST_MODE $COMPUTE\n"

