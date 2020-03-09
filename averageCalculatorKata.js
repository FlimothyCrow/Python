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
  var modeArray = [];
  var intsObject = {};
  for (number of listOfInts){
    intsObject[number] = (intsObject[number]+1) || 1 ;
  }
  for (pair of Object.entries(intsObject)){
    if (pair[1] > 1){
      modeArray.push(pair)
    }
  }
  return modeArray
}

function hasDupes(listOfInts){
  const yesDupes = new Set(listOfInts)
  return yesDupes
}
