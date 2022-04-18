
function download_python() {

}

mkdir ~/code

Build from source python 3.7, install with prefix to ~/.python folder:

wget --no-check-certificate https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz ; \
tar xvf Python-3.7.* ; \
cd Python-3.7.3 ; \
mkdir ~/.python ; \
./configure --enable-optimizations --prefix=/home/www/.python --with-ensurepip=install ; \
make -j8 ; \
sudo make altinstall