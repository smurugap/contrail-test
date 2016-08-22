

. /etc/contrail/openstackrc
#export PYTHONPATH=./fixtures:./scripts:./:./vnc_api-0.1dev:./cfgm_common-0.1dev:/usr/lib/python2.7/dist-packages/
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bgp_ntt.yaml  --delete --tenant_name=ALL 
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.nogw.yaml  --delete_global
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bgp_ntt.yaml  --create_global
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bgp_ntt.yaml  --create --tenant_count 30 --tenant_index_range 1:30
#sleep 120
#for i in {1..100}; do
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.bgp_ntt.yaml --traffic_only --tenant_index_range 300:320
#done
