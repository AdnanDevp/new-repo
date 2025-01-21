#!/bin/bash

echo "Ciau tutti!"

redis-server --daemonize yes

cd /home/$USER/Code/AIM_testo/

# cd /home/$USER/Dokumente/Code/Python/AIM/AIM_ml_userinterface/

conda activate ./.venv_testo/
export FLASK_DEBUG=1
python src/dash_app.py
