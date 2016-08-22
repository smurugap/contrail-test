#cp diagnostics/systemtest.py diagnostics/systemtest.py.working
#cp diagnostics/config.py diagnostics/config.py.working
#scp diagnostics/systemtest.py.working diagnostics/config.py.working 10.87.129.2:/cloud/vageesant/ceph/fab_ci_jenkin/contrail-test-smurugap/contrail-test/diagnostics/
scp -r diagnostics/* 10.87.129.2:/cloud/vageesant/ceph/fab_ci_jenkin/contrail-test-smurugap/contrail-test/diagnostics/
scp -r * 10.87.129.2:/cloud/vageesant/ceph/fab_ci_jenkin/contrail-test-smurugap/contrail-test
