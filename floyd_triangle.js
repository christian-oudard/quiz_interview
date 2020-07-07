function floyd(numRows) {
  var rowLen, x, i = 0
  for (rowLen = 1; rowLen <= numRows; rowLen++) {
    var row = new Array()
    for (x = 0; x < rowLen; x++) {
      i += 1
      row.push(i)
    }
    console.log(row.join(' '))
  }
}

floyd(5)
