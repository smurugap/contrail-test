
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

ulimit -n 65535

python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/simple.yaml --create --tenant_index_range 651:652  --tenant_count 1 
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/simple.yaml --traffic_only --tenant_index_range 651:652  --tenant_count 1 --feature_ping_only
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/simple.yaml --create --tenant_index_range 651:652  --tenant_count 1 
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.full.yaml  --create_global 
exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/simple.yaml --delete --tenant_name=ALL_TEST 
#exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/simple.yaml --create --tenant_index_range 650:651  --tenant_count 1 --debug
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/simple.yaml --delete --tenant_index_range 175:651  --tenant_count 1 
exit
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --traffic_only --tenant_index_range 320:330  --tenant_count 1 --loop_count 10
exit


#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol2.global.yaml --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_index_range 600:610  --tenant_count 1
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol2.global.yaml --yaml_config_file diagnostics/symantec.full.yaml --create --tenant_index_range 600:610  --tenant_count 1
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --create --tenant_index_range 600:610  --tenant_count 10

while true;
do
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --traffic_only --tenant_index_range 600:610  --tenant_count 10
sleep 10
done


