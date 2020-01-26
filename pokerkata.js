
      // This is what a simple unit test looks like:

      function cardValue(card) {
        if (card[0] === "A") {
            return 14
        }
        else if (card[0] === "K") {
            return 13
        }
        else if (card[0] === "Q") {
            return 12
        }
        else if (card[0] === "J") {
            return 11
        }
        else return parseInt(card.slice(0, -1))
      }


      function makeCard(string) {
        return { value : cardValue(string), suit : string.charAt(string.length-1)  }
      }


      function makeHand(listOfCards) {
        var handObject = []
        for (card of listOfCards) {
          handObject.push(makeCard(card))
        }
        return { cards : handObject }
      }
// ----------------------------------------------------------
      function isMatch(hand) {
        var listOfValues = {} ;
        for (card of hand.cards) {
          listOfValues[card.value] = (listOfValues[card.value]+1) || 1 ;
          }
          var counter = 0 ;
          for (let i = 0; i < listOfValues.length; step++) {
              if (listOfValues[i].value === 2) {
                counter += 1
              }
          }
          if (counter === 2) {
            return "string"
          }
        for (key in listOfValues) {
          if (listOfValues[key] === 2) {

            return "pair of " + key
          }
          else if (listOfValues[key] === 3) {
            return "three of " + key
          }
          else if (listOfValues[key] === 4) {
            return "four of " + key
          }
        }

        return listOfValues
      };
