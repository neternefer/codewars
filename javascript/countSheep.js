function countSheeps(arrayOfSheep) {
    //Count the number of sheep present in the array (true means present).
    return arrayOfSheep.filter((e) => e == true).length;
  }

countSheeps([true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true]) //17