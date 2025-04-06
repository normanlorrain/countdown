# Linux tips

## Helpful packages

```
sudo apt update
sudo apt upgrade
sudo apt install pipx openssh-server samba
```
## Ubuntu/Gnome

***~/.config/autostart/countdown.desktop***

```ini
[Desktop Entry]
Type=Application
Exec=countdown /home/norman/country-flags/png1000px/
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=countdown
Name=countdown
Comment[en_US]=testing
Comment=testing
```

## Ubuntu/LxQt

***.config/autostart/countdown.desktop***

```ini
[Desktop Entry]
Exec=countdown -c /home/norman/countdown.toml
Name=countdown
Type=Application
Version=1.0
X-LXQt-Need-Tray=true
```
