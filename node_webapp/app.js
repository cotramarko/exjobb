var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

/*
var routes = require('./routes/index');
var users = require('./routes/users');
var search = require('./routes/search');
*/

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

/*
app.use('/', routes);
app.use('/users', users);
app.use('/searching', search);
*/

app.get('/', function(req, res) {res.render('index', { title: 'Express', scripts: ['javascripts/main.js']});
});

app.get('/home', function(req, res) {res.render('home', { title: 'Metro GUI', scripts: ['javascripts/home.js']});
});

app.get('/list', function(req, res) {
          
  // var json = JSON.parse(require('fs').readFileSync('./public/exjobb.json', 'utf8'))
  var db = require('mongoskin').db('mongodb://localhost:27017/exjobb');
  var coll = db.collection('dataset');
    coll.find({}, { _id:0}).toArray(function(err, result) {
      if (err) throw err;    
      res.send(result);
    });

});

app.get('/exjobb', function(req, res) {
      
//  var json = JSON.parse(require('fs').readFileSync('./public/exjobb.json', 'utf8'))
    var db = require('mongoskin').db('mongodb://localhost:27017/exjobb');

    var page = req.query.page;
    var results_per_page = 5;
    var offset = page*results_per_page;
    console.log(page);
    var coll = db.collection('dataset');
    coll.find({}, { _id:0}).skip(offset).limit(results_per_page).toArray(function(err, result) {
      if (err) throw err;
      //console.log(result);

      coll.find({}, { _id:0}).count(function(err, count) {
          console.log(Math.floor(count/results_per_page));
    

          res.render('exjobb', {data : result, page_counter : Math.floor(count/results_per_page)});

      });
    
});      



});

app.get('/marko', function(req, res) {
      
  var json = JSON.parse(require('fs').readFileSync('./public/exjobb.json', 'utf8'))
      
      res.render('exjobb_marko', {data : json});

});

app.get('/angular', function(req, res) {
      
      res.render('angular', {});

});



// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});


module.exports = app;

//     var db = require('mongoskin').db('mongodb://localhost:27017/transport');

//     db.collection('transport').find({}, { _id:0}).toArray(function(err, result) {
//     if (err) throw err;
//     var foo = 'hej';
//     console.log(result);
//     res.render('list', {data : result});
// });

