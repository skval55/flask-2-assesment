function starOutGrid(grid) {
  const finalGrid = [];
  for (i = 0; i < grid.length; i++) {
    const index = grid[i].indexOf("*");
    if (index >= 0) {
      grid[i] = ["*", "*", "*"];
      finalGrid.push(index);
    }
  }
  for (i = 0; i < grid.length; i++) {
    for (num of finalGrid) {
      grid[i][num] = "*";
    }
  }
  return grid;
}
