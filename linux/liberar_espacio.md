```bash
du -h --max-depth=1

sudo apt-get clean
sudo apt-get autoclean

sudo apt-get autoremove

sudo du -h /var/log
sudo truncate -s 0 /var/log/*   # Clears log files

rm -rf ~/.local/share/Trash/*

sudo find /tmp -type f -size +10M
```
