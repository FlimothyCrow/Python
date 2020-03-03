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
  modeList = []
  for (i = 0; i < listOfInts.length; i++){
    if (listOfInts[i] === listOfInts[i+1]){
      modeList.push(listOfInts[i])
    }
  }
  return modeList
}
