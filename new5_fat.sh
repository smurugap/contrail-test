
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

ulimit -n 65535

rm ping_result_symantec.Tenant.201.txt

if [ "$1" = 'feature_ping_only' ];
then
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.fat.yaml --create --tenant_count 1 --tenant_index_range 201:210 
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.fat.yaml --traffic_only --tenant_index_range 201:210  --tenant_count 1 --feature_ping_only

exit
fi


while true;
do
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.fat.yaml --delete --tenant_count 1 --tenant_index_range 200:210
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.fat.yaml --create --tenant_count 1 --tenant_index_range 200:210
 for i in {1..10}
   do
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.fat.yaml --traffic_only --tenant_index_range 200:210  --tenant_count 1
 sleep 10
done
done



