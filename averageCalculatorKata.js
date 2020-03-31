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

function removeDupes(listOfInts){
  const yesDupes = Array.from(new Set(listOfInts))
  return yesDupes
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
  var filteredList = ints.filter(x => x % 2 !== 0)
  return filteredList
}
