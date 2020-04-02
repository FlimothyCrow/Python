test('averageCalculator', function(assert) {
  var listOfInts = averageCalculator([1, 10])
  assert.equal(listOfInts, 5.5) ;
});

test('averageCalculator0', function(assert) {
  var listOfInts = averageCalculator([1, 10, 100, 5, 39])
  assert.equal(listOfInts, 77.5) ;
});
//---------------------------------------

test('meanCalculator', function(assert){
  var listOfInts = meanCalculator([1, 2, 3, 4, 5, 6])
  assert.equal(listOfInts, "pass") ;
});

test('meanCalculator', function(assert){
  var listOfInts = meanCalculator([1, 2, 3, 4, 5])
  assert.equal(listOfInts, 3) ;
});

test('meanCalculator', function(assert){
  var listOfInts = meanCalculator([1, 2, 3, 4, 5, 6, 7, 8, 9])
  assert.equal(listOfInts, 5) ;
});
//---------------------------------------

test('modeCalculator', function(assert){
  var listOfInts = modeCalculator([1, 9, 1, 2, 9, 39, 238]) ;
  assert.deepEqual(listOfInts, [["1",2], ["9",2]])
})
//---------------------------------------

test('removeDupes', function(assert){
  var listDupes = removeDupes([1, 2, 1, 1, 3, 4, 3, 9, 3]);
  assert.deepEqual(listDupes, [1, 2, 3, 4, 9])
})
//---------------------------------------
test('sumReduce0', function(assert){
  var listDupes = sumReduce([5, 10, 20]);
  assert.deepEqual(listDupes, 35)
})
//---------------------------------------
test('filterEvens0', function(assert){
  var listOfInts = filterEvens([5, 9, 10, 20, 39]);
  assert.deepEqual(listOfInts, [5, 9, 39])
})
//---------------------------------------
test('filterEvens00', function(assert){
  var listOfInts = filterEvens0([5, 9, 10, 20, 39]);
  assert.deepEqual(listOfInts, [5, 9, 39])
})
