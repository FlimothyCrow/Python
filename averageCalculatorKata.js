

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

function removeDupes(listOfInts){
  return Array.from(new Set(listOfInts))
}

function sumReduce(ints){
  return ints.reduce((acc, next) => acc + next)
}

function filterEvens(ints){
  var filteredList = ints.reduce((acc, next) => {
    if (next % 2 !== 0){
      acc.push(next)
    }
      return acc
  }, [])
  return filteredList
}

function filterEvens0(ints){
   return ints.filter(x => x % 2 !== 0)
}

function averageCalculator(integers) {
  return integers.reduce((acc, next) => acc + next) / 2
}
