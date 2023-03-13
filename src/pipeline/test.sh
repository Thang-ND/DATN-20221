echo "START DATA FLOW"
cd /home/thangnd/Documents/20221/DATN-20221/src/pipeline
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/cellphoneS.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/tragopdidong.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/dienmaycholon.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/oneway.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/store24h.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/thegioididong.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/viettablet.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/viettel_store.py
/home/thangnd/anaconda3/envs/crawler/bin/python3 /home/thangnd/Documents/20221/DATN-20221/src/pipeline/xtmobile.py
echo "FINISH DATA FLOW"