var app = angular.module('myApp', []);
app.controller('exjobbCtrl', function($scope, $http) {
    $scope.query = "";
    $http.get("/list").then(function(response) {
    $scope.myWelcome = response.data;
    });
    $scope.filterList = function(x){
    console.log($scope.query);
    console.log(x.company);
    return (x.title.toLowerCase().indexOf($scope.query) != -1) || 
        (x.location.toLowerCase().indexOf($scope.query) != -1) ||
        (x.company.toLowerCase().indexOf($scope.query) != -1);
    };
});