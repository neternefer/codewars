//Fix getNames function -> map always needs return
function getNames(data){
    return data.map(function(item){return item.name});
  }