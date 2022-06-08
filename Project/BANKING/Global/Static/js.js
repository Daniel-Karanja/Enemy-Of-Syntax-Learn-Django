// document.addEventListener("DOMContentLoaded", () => {
//   closeMessageBox();
// });

function closeMessageBox() {
  box = document.getElementById("mess_box");
  setTimeout(() => {
    box.style.display = "none";
  }, 15000);
}

closeMessageBox();
