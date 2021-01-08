#!/bin/sh


python3.8 spectral.py ccc_ado 100 > ado_spectral_KM_100
python3.8 spectral.py ccc_ado 200 > ado_spectral_KM_200

python3.8 spectral_DS.py ccc_ado 100 > ado_spectral_DS_100
python3.8 spectral_DS.py ccc_ado 200 > ado_spectral_DS_200
