function averageCalculator(integers) {
  sumOfInts = 0
  for (int of integers){
    sumOfInts += int
  }
  return sumOfInts / integers.length
}

function meanCalculator(listOfInts){
  if (listOfInts.length % 2 === 0){
    return "pass"
  }
  else {
    return listOfInts[(listOfInts.length / 2) - 0.5]
  }
}

function modeCalculator(listOfInts){
  var modeObject = {};
  for (number of listOfInts){
    modeObject[number] = (modeObject[number]+1) || 1 ;
  }
  return modeObject
}
