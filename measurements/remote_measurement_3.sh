# Taking the measurement
echo "Hello from remote_measurement_3.sh"
cd 0_ba/bachelor_thesis
git pull
git fetch
cd measurements
source measurement_3.conf
export remote_measurement=0
source measurement_3.sh

# Sync the changes
echo "Pushing bachelor thesis files to github..."
cd ~/0_ba/bachelor_thesis
git add .
git commit -m "automatic measurement push"
cd measurements
#source remote_push.sh
