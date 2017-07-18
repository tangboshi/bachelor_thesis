# Taking the measurement
echo "Hello from remote_measurement.sh"
cd 0_ba/bachelor_thesis
git pull
git fetch
cd measurements
source measurement.conf
export remote_measurement=0
source measurement.sh

# Sync the changes
echo "Pushing bachelor thesis files to github..."
cd ~/0_ba/bachelor_thesis
git add .
git commit -m "automatic measurement push"
cd measurements
#source remote_push.sh
