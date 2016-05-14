var app = angular.module('myApp', ['ngMaterial']);
app.controller('exjobbCtrl', function($scope, $http) {
    $scope.query = "";
    $http.get("/list").then(function(response) {
    $scope.myWelcome = response.data;
    });
    String.prototype.capitalizeFirstLetter = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
    }
    $scope.filterList = function(x){
    //console.log($scope.query);
    //console.log(x.company);
    return (x.title.toLowerCase().indexOf($scope.query) != -1) || 
        (x.location.toLowerCase().indexOf($scope.query) != -1) ||
        (x.company.toLowerCase().indexOf($scope.query) != -1);
    };
});

app.controller('DemoCtrl', DemoCtrl);
  function DemoCtrl ($timeout, $q, $log, $scope) {
    var self = this;
    self.simulateQuery = false;
    self.isDisabled    = false;
    // list of `state` value/display objects
    self.states        = loadAll();
    self.querySearch   = querySearch;
    self.selectedItemChange = selectedItemChange;
    self.searchTextChange   = searchTextChange;
    self.newState = newState;
    self.clear = clear;
    $scope.showLocation = false;
    function newState(state) {
      alert("Sorry! You'll need to create a Constituion for " + state + " first!");
    }
    // ******************************
    // Internal methods
    // ******************************
    /**
     * Search for states... use $timeout to simulate
     * remote dataservice call.
     */
    function querySearch (query) {
      var results = query ? self.states.filter( createFilterFor(query) ) : self.states,
          deferred;
      if (self.simulateQuery) {
        deferred = $q.defer();
        $timeout(function () { deferred.resolve( results ); }, Math.random() * 1000, false);
        return deferred.promise;
      } else {
        return results;
      }
    }
    function searchTextChange(text) {
      $log.info('Text changed to ' + text);
    }
    function selectedItemChange(item) {
      if (item != null) {
        $log.info('Item changed to ' + JSON.stringify(item));
        $scope.Location = item.value.capitalizeFirstLetter();
        $scope.showLocation = true;  
        self.clear();
      }
      
      
    }
    function clear() {
      self.selectedItem = null;
      self.searchText = "";
      //self.display = "";
    }
    /**
     * Build `states` list of key/value pairs
     */
    function loadAll() {
      var allStates = 'Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware,\
              Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana,\
              Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana,\
              Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina,\
              North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina,\
              South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia,\
              Wisconsin, Wyoming';
      return allStates.split(/, +/g).map( function (state) {
        return {
          value: state.toLowerCase(),
          display: state
        };
      });
    }
    /**
     * Create filter function for a query string
     */
    function createFilterFor(query) {
      var lowercaseQuery = angular.lowercase(query);
      return function filterFn(state) {
        return (state.value.indexOf(lowercaseQuery) === 0);
      };
    }
  }
