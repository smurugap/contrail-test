
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log
ulimit -n 65535
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.mirror.yaml --traffic_only --tenant_index_range 360:370  --tenant_count 1 --loop_count 10
exit

if [ "$1" = 'feature_ping_only' ];
then
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.mirror.yaml --create --tenant_count 1 --tenant_index_range 360:370
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.mirror.yaml --traffic_only --tenant_index_range 360:370  --tenant_count 1 --loop_count 10 --feature_ping_only

exit
fi

while true;
do
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.mirror.yaml --delete --tenant_count1 --tenant_index_range 360:370
sleep 600
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.mirror.yaml --create --tenant_count 1 --tenant_index_range 360:370
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.mirror.yaml --traffic_only --tenant_index_range 360:370  --tenant_count 1 --loop_count 10
sleep 10
done


