var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/searching', function(req, res){
 res.send("WHEEE");
});
module.exports = router;

