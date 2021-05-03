# Alarm Server

This is a simple python script to provide a web socket server to add, stop and
list alarms.  The alarm sound will be played on the machine where this server is
running.


## How to install

You can use the provided `PKGBUILD` for Arch Linux, or install it manually.

### Install via `PGKBUILD`

Create a package with `makepkg` and then install it.

To enable the systemd daemon, execute:
```
# systemctl enable alarm-server.service
```

### Install manually

Install all dependencies and your audio system of choice.

#### Dependencies:
* python >= 3.9
* python-websockets >= 8.1
* python-simpleaudio >= 1.0.4

If you want to use `systemd` to autostart the server on boot, make sure to
adjust the path to the server script, then copy it manually to
`/usr/lib/systemd/system` and enable it via:
```
# systemctl enable alarm-server.service
```


## Configuration

Before you start the server for the first time you need to add the configuration
file.  You can copy the provided template file in the root directory:
```
# cp config.ini.dist config.ini
```

There are two configuration values, the web socket server port, and the alarm
sound file name.

Default port: `12614`

### Sound file

Copy your alarm sound file in the `sound/` directory in the project.  It needs
to be a `.wav` file.  Then specify the file name in the configuration.


## Command list on the web socket server

* play
* stop
* timer 10(s|m|h)
* timer 16:20
* timer_repeat 10(s|m|h)
* timer_repeat 16:20
* timer_stop 10(s|m|h)
* timer_stop 16:20
* timer_stop_repeat 10(s|m|h)
* timer_stop_repeat 16:20
* list

An added timer needs to be stopped with the exact same time phrase.

#### Example:
Timer added: ```timer 6:30```

Timer stopped: ```timer_stop 6:30```

Starting the timer with `6:30` and stopping it with `06:30` doesn't work.


## Timer list

When a `list` command was sent, the server sends a reply with every active
timer, one per line.

Example:
```
timer 6:30;2021-05-01 06:30:00
timer_repeat 1h;2021-05-01 10:05:02
```

The first part is the timer key, the second part, separated with a semicolon,
is the next alarm date for the timer.


## Clients

A simple console client script can be used with the `client.py` file.

There's also a react js web interface, available [here](https://github.com/holloway87/alarm-server-web-client).
