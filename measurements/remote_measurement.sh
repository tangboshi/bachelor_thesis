# Taking the measurement
echo "Hello from remote_measurement.sh"
cd 0_ba/bachelor_thesis
git pull
git fetch
cd measurements
source measurement.conf
export REMOTE_MEASUREMENT=0
source measurement.sh

# Sync the changes
echo "Pushing bachelor thesis files to github..."
cd ~/0_ba/bachelor_thesis
git add .
git commit -m "automatic measurement push"
git push https://tangboshi:03c3f27f1a76830e0d12239599cc57b9d0c7fc69@github.com/tangboshi/bachelor_thesis.git
