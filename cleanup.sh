
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./
rm logs/tor-scale.log.log
#python diagnostics/cleanup.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.snat.yaml
python diagnostics/cleanup.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml
