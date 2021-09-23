
var assert = require('assert');
var parityAnaly = require('./parityAnalysis')
describe('parityAnalysis(n)', function() {
  it('should return true when the value is 1145', function() {
    assert.equal(parityAnaly.parityAnalysis(1145), true);
  });
  it('should return false when the value is 789', function() {
    assert.equal(parityAnaly.parityAnalysis(789), false);
  });
  it('should return false when the value is 15', function() {
    assert.equal(parityAnaly.parityAnalysis(15), false);
  });

  it('should return true when the value is 7', function() {
    assert.equal(parityAnaly.parityAnalysis(7), true);
  });
  it('should return true when the value is 112', function() {
    assert.equal(parityAnaly.parityAnalysis(112), true);
  });




});  
