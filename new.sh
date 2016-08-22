

. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api-0.1dev:./cfgm_common-0.1dev:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bms.yaml  --delete --tenant_name ALL
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.psvn.yaml  --delete --tenant_index_range 100:100 --tenant_count 1 
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bms.yaml  --delete_global
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bms.yaml  --create_global
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bms.yaml  --create --tenant_count 1 --tenant_index_range 20:20 
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.psvn.yaml --traffic_only --tenant_index_range 0:0 --tenant-count 1 
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bms.yaml --traffic_only --tenant_index_range 20:20 
