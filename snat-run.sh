
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./
rm logs/tor-scale.log.log
python diagnostics/snat-systemtest.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/snat-symantec.yaml

