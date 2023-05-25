const fs = require('fs')
const file = 'world.topo.bathy.200411.3x5400x2700.bmp'
const readStream = fs.createReadStream('file')
let size = 0
readStream.on('data', data => {
    size += data.length

})
readStream.on('end', () => {
    console.log(size/1024/1024)
})