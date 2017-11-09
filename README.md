# divicaubot
My very first bot for Telegram written in Python.

This bot basically get's a magnet link with the _/magnet_ command, converts (download metadata actually) to a torrent file and pass it to the bittorrent client included. Then, the file (or the files) is(are) downloaded and sent to the chat. 

If multiple files are in the torrent, only the heavier is sent. This is, if you download a film for example, you only want the film itself, not the readme files within the torrent.
* The magnet_to_torrent2 source is from [Dan Folkes' github](https://github.com/danfolkes/Magnet2Torrent)
* The bittorrent client is from a [stack overflow's answer](https://stackoverflow.com/a/5494823/5620997). I modified it a bit to fit my project.
