
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

ulimit -n 65535

rm ping_result_symantec.Tenant.350.txt

if [ "$1" = 'feature_ping_only' ];
then
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v2.yaml --create --tenant_count 1 --tenant_index_range 350:360 --dpdk
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v2.yaml --traffic_only --tenant_index_range 350:360  --tenant_count 1 --loop_count 10 --feature_ping_only

exit
fi

while true;
do
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v2.yaml --delete --tenant_count 1 --tenant_index_range 350:360
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v2.yaml --create --tenant_count 1 --tenant_index_range 350:360
for i in {1..10}
do
   python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.ipv6.v2.yaml --traffic_only --tenant_index_range 350:360  --tenant_count 1 --loop_count 10
sleep 10
done
done


