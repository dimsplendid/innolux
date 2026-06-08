// use for innolux mailbox format bookmark plug
(() => {
  const topDoc = window.top.document;
  let allframe = topDoc.getElementById('allframe');
  allframe.cols = "300, 0, *";
  let leftSide = topDoc.getElementById('leftSide');
  leftSide.rows = "0, *, 180";

  const folderDoc = topDoc.getElementById('foldermenu').contentDocument;
  const mailbox = folderDoc.querySelector("#mailbox");
  const closebutton = folderDoc.querySelector("#closebutton");
  mailbox.style = "display:block";
  closebutton.style = "display:block";
})()
