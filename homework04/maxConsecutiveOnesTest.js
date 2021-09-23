var assert = require('assert');
var maxConsec = require('./maxConsecutiveOnes')
describe('maxConsecutiveOnes(n)', function() {
  it('should return 4 when the value is [1,0,1,1,1,0,1,1,1,1]', function() {
    assert.equal(maxConsec.maxConsecutiveOnes([1,0,1,1,1,0,1,1,1,1]), 4);
  });
  it('should return 4 when the value is [1,1,1,0,0,1,0,1,1,1,1]', function() {
    assert.equal(maxConsec.maxConsecutiveOnes([1,1,1,0,0,1,0,1,1,1,1]), 4);
  });
  it('should return 2 when the value is [1,0,1,0,1,1]', function() {
    assert.equal(maxConsec.maxConsecutiveOnes([1,0,1,0,1,1]), 2);
  });

});  
