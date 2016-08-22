

. /etc/contrail/openstackrc
#export PYTHONPATH=./fixtures:./scripts:./:./vnc_api-0.1dev:./cfgm_common-0.1dev:/usr/lib/python2.7/dist-packages/
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml  --delete --tenant_name=ALL
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml  --delete --tenant_index_range 60:61 
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml  --delete_global
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml  --create_global
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml  --create --tenant_count 1 --tenant_index_range 600:601 
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml --traffic_only --tenant_index_range 100:101
