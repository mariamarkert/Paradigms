// Generated by CoffeeScript 1.6.3
(function() {
  var changeEnough;

  changeEnough = function(changeInPocket, amount) {
    var ret, totalChange;
    ret = false;
    totalChange = changeInPocket[0] * .25 + changeInPocket[1] * .1 + changeInPocket[2] * .05 + changeInPocket[3] * .01;
    if (totalChange >= amount) {
      ret = true;
    }
    return ret;
  };

  module.exports = {
    changeEnough: changeEnough
  };

}).call(this);
