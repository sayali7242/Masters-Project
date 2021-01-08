#!/bin/sh


python3.8 spectral.py ccc_gru 100 > gru_spectral_KM_100
python3.8 spectral.py ccc_gru 200 > gru_spectral_KM_200

python3.8 spectral_DS.py ccc_gru 100 > gru_spectral_DS_100
python3.8 spectral_DS.py ccc_gru 200 > gru_spectral_DS_200
