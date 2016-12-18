var express = require('express');
var request = require('request');
var http = require("http");

var router = express.Router();
/* GET users listing. */

function makeRequest(data, callback) {
  
  var options = {
    hostname: 'localhost',
    port: 5000,
    path: '/analyze',
    method: 'POST',
    headers: {
      'Content-Type': 'text/plain',
    }
  };
  var req = http.request(options, function (res) {
    console.log('Status: ' + res.statusCode);
    console.log('Headers: ' + JSON.stringify(res.headers));
    res.on('data', function (body) {
      callback(body);
    });
  });
  req.on('error', function (e) {
    callback(e);
  });
  // write data to request body
  req.write(data);
  req.end();
}

//req.body
router.get('/', function (req, res, next) {
  
  request.post({
    headers: { 'content-type': 'text/plain' },
    url: 'http://localhost:5000/analyze',
    body: "I wonder if the wildly different media coverage on both caused that Bwahaha sarcasm"
  }, function (error, response, body) {
    res.send(body);
  });

});

router.post('/', function (req, res, next) {
  var data = req.body.data;
  request.post({
    headers: { 'content-type': 'text/plain' },
    url: 'http://localhost:5000/analyze',
    body: data
  }, function (error, response, body) {
    res.send(body);
  });

});

module.exports = router;
