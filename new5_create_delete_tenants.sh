
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log
rm ping_result_symantec.Tenant.150.txt
ulimit -n 65535

if [ "$1" = 'feature_ping_only' ];
then
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.yaml --create --tenant_index_range 150:152  --tenant_count 1
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.yaml --traffic_only --tenant_index_range 150:152  --tenant_count 1 --loop_count 2 --feature_ping_only
exit
fi

while true;
do
   python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.yaml --create --tenant_index_range 150:152  --tenant_count 1
   sleep 10
   for i in {1..10}
    do
   python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.yaml --traffic_only --tenant_index_range 150:152  --tenant_count 1 --loop_count 2
   sleep 10
   done
   python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.yaml --delete --tenant_index_range 150:152  --tenant_count 1
done
