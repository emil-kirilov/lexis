var express = require('express');
var router = express.Router();
/* GET users listing. */
router.get('/', function (req, res, next) {

  pyshell.send('hello');
  pyshell.on('message', function (message) {
    res.send(message);
    console.log(message);
  });
});

module.exports = router;
