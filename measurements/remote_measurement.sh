echo "Hello from remote_measurement.sh"
cd 0_ba/bachelor_thesis
git pull
git fetch
cd measurements
source measurement.conf
export REMOTE_MEASUREMENT=0
source measurement.sh
