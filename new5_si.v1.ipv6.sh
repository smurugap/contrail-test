
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log
ulimit -n 65535

if [ "$1" = 'feature_ping_only' ];
then
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v1.yaml --create --tenant_count 2 --tenant_index_range 330:340 --dpdk
  
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v1.yaml --traffic_only --tenant_index_range 330:340  --tenant_count 2 --loop_count 10 --feature_ping_only
exit
fi

while true;
do
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v1.yaml --delete --tenant_count 1 --tenant_index_range 330:340
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v1.yaml --create --tenant_count 1 --tenant_index_range 330:340
  
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v1.yaml --traffic_only --tenant_index_range 330:340  --tenant_count 1 --loop_count 10
sleep 10
done


