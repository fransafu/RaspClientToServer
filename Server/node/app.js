const express = require('express')
const app = express()

app.get('/RaspIP', function (req, res) {
  res.send('Ok!')
})

app.listen(3080, function () {
  console.log('Server on port 3080')
})
