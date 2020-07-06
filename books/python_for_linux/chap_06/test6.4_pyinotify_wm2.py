import pyinotify

wm = pyinotify.WatchManager()
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE
wm.add_watch('/tmp', mask)

notifier = pyinotify.Notifier(wm)
notifier.loop()
