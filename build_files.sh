# build_files.sh
apt-get install libsqlite3-dev
pip install -r requirements.txt
python3 manage.py collectstatic
