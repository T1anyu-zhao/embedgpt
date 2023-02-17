var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express1' });
  // res.send('Got a get request')
});
router.post('/', (req, res) => {
  res.send('Got a POST request')
})

module.exports = router;
