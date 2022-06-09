let chess_table = document.getElementById("chess_table");

function createTable(r, c) {
  let row_counter = 0;
  for (let i = 0; i < r; i++) {
    let row = document.createElement("div");
    row.classList.add("w3-border", "chess-row");
    row_counter = i;
    for (let j = 0; j < c; j++) {
      let col = document.createElement("div");

      if (row_counter % 2 === 0) {
        // I is odd
        col.classList.add("cell", "w3-blue");
      } else {
        col.classList.add("cell");
      }
      col.innerText = `x${j},y${i}`;
      col.setAttribute("onClick", `cellClick(${i},${j})`);
      row.appendChild(col);
      row_counter++;
    }
    chess_table.appendChild(row);
  }
}

function cellClick(i, j) {
  console.log(`x${j},y${i}`);
}

createTable(8, 8);
