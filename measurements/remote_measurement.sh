# Taking the measurement
echo "Hello from remote_measurement.sh"
cd 0_ba/bachelor_thesis
# git pull
# git fetch
cd measurements
source measurement.conf
export REMOTE_MEASUREMENT=0
source measurement.sh

# Sync the changes
echo "Pushing bachelor thesis files to github..."
cd ~/0_ba/bachelor_thesis
git add .
git commit -m "automatic measurement push"
git push https://tangboshi:042c7444fecad76415b61fa22c4baee21f9c09e0@github.com/tangboshi/bachelor_thesis.git
