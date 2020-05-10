

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

function averageCalculator(integers) {
  return integers.reduce((acc, next) => acc + next) / 2
}

function meanCalculator(listOfInts){
  if (listOfInts.length % 2 === 0){
    return "pass"
  }
  else {
    return listOfInts[(listOfInts.length / 2) - 0.5]
  }
}
function filterEvens0(ints){
   return ints.filter(x => x % 2 !== 0)
}

function filterFactor(targetFactor, listOfIntegers){
  return listOfIntegers.filter(x => x % targetFactor === 0)
}
// --------------------------------------------------------
function fizzBuzzNoveau(targetRange){
  var spicy = Array.from(Array(10)).map((e,i)=>i+1)  // [0, 1, 2...]
  return spicy.map((element) => {
    if (element % 2 === 0 && element % 3 === 0){
      return "fizzBuzz"
    }
    else if (element % 3 === 0){
      return "fizz"
    }
    else if (element % 2 === 0){
      return "buzz"
    }
    else {
      return element
    }
  })
}
// map does not mutate, it clones
console.log(Array.from(Array(10)).map((e,i)=>i+1))

function objectify(listOfInts){
  return listOfInts.map((x) => ({id:x}))
}
// --------------------------------------------------------
function select(listOfObjects, target){
  return listOfObjects.map(object => {
    if (object.id === target){
      return {
        id:target,
        selected:true
      }
    }
    return {
      id:object.id,
      selected:false
    }
  })
}
// --------------------------------------------------------
function selectedMover(list0, list1){
  array0 = []
  array1 = []
  rearrangedArray = []
  list0.map((object) => {
    if (object.selected === true){ // if the object is "selected"
      array1.push(object)
    }
    else {
      array0.push(object)
    }
  })
  list1.map((object) => {
    if (object.selected === true){ // if the object is "selected"
      array0.push(object)
    }
    else {
      array1.push(object)
    }
  })
  return array0
}
