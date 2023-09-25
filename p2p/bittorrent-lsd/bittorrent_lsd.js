#!/usr/bin/env node


//import 'bittorrent-lsd';
//import * as name from 'bittorrent-lsd';


const opts = {
  peerId: new Buffer('01234567890123456789'), // hex string or Buffer
  infoHash: new Buffer('01234567890123456789'), // hex string or Buffer
  port: 6771 //common.randomPort() // torrent client port
  // https://www.bittorrent.org/beps/bep_0014.html
}

const lsd = new LSD(opts)

// start getting peers from local network
lsd.start()

lsd.on('peer', (peerAddress, infoHash) => {
  console.log('found a peer: ' + peerAddress)
})

lsd.destroy()


