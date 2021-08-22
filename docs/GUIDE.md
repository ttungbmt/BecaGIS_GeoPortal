# BecaGIS_GeoPortal

```shell
# Create Env
sudo mkdir -p ~/VNTT/BecaGIS_GeoPortal
sudo usermod -a -G www-data $USER;
sudo chown -Rf $USER:www-data ~/VNTT/BecaGIS_GeoPortal
sudo chmod -Rf 775 ~/VNTT/BecaGIS_GeoPortal

python -m venv ~/VNTT/.virtualenvs/geoportal
source ~/VNTT/.virtualenvs/geoportal/bin/activate
#pip install Django==3.2


git clone https://github.com/GeoNode/geonode-project.git -b 3.1.x
django-admin startproject --template=./geonode-project -e py,sh,md,rst,json,yml,ini,env,sample,properties -n monitoring-cron -n Dockerfile geoportal

git clone https://github.com/ttungbmt/geonode.git -b 3.1.x

# Install the Python packages
cd ~/VNTT/BecaGIS_GeoPortal/geoportal
pip install -r requirements.txt --upgrade --no-cache --no-cache-dir
pip install -e . --upgrade
```





```shell
sudo rm -rf ~/VNTT/.virtualenvs/geoportal
```