import pyinotify

wm = pyinotify.WatchManager()
wm.add_watch('/tmp', pyinotify.ALL_EVENTS)

notifier = pyinotify.Notifier(wm)
notifier.loop()
