//Return filtered array without geese
function gooseFilter (birds) {
    var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
    let result = birds.filter(function(n){
      return !(geese.includes(n))
      })
    return result

  };
