Panthera buildZip tool
========

[Panthera Framework](https://github.com/Panthera-Framework/panthera) archive builder. 
Builds tar.gz and zip archives with all dependencies resolved from git branch of Panthera Framework.

##Requirements

- Python 2.7 or Python 3
- [Panthera Desktop](https://github.com/Panthera-Framework/Panthera-Desktop)

##Installation 
```bash
cd /tmp
git clone https://github.com/Panthera-Framework/buildZip
cd buildZip
sudo ./setup.py install
```

##Usage

```bash
# Build both zip and tar.gz archives
panthera-buildZip --zip /tmp/panthera.zip --targz /tmp/panthera.tar.gz

# Build only tar.gz archive
panthera-buildZip --targz /tmp/panthera.tar.gz
```
