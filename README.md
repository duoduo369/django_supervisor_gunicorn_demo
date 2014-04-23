django gunicorn supervisor demo
===

usage
---

git clone <项目地址> ~/supervisor_demo
sudo ln -s ~/supervisor_demo /opt

pip install virtualenv
mkdir ~/python_evn
sudo ln -s ~/python_evn /opt
cd /opt/python_evn
virtualenv django1.6.1

pip install -r requirements.txt

cd /opt/supervisor_demo/supervisor
supervisord

访问[127.0.0.1:8001](http://127.0.0.1:8001)
之后可以在此目录启用supervisorctl查看项目状态
