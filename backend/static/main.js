var dropZone = document.querySelector(".drop-zone");
var fileInput = document.querySelector("#fileInput");
var browseBtn = document.querySelector("#browseBtn");
var msgdiv = document.querySelector("#msgbox");
var maxSize = 50 * 1024 * 1024; 

browseBtn.addEventListener('click',function(){
  fileInput.click();
});

fileInput.addEventListener('change',function(){
  document.getElementById('uploadfilebtn').click();
});
dropZone.addEventListener("drop", function(e){
  e.preventDefault();
  const files = e.dataTransfer.files;
  if (files.length === 1) {
    if (files[0].size < maxSize) {
      fileInput.files = files;
      uploadFile();
    } else {
      showmsg("Max file size is 50MB");
    }
  } else if (files.length > 1) {
    showmsg("Sorry, multiple file upload will be in next update.");
  }
  dropZone.classList.remove("dragged");
});


dropZone.addEventListener("dragover", function(e){
  e.preventDefault();
  dropZone.classList.add("dragged");
});

dropZone.addEventListener("dragleave", function(e){
  dropZone.classList.remove("dragged");
  console.log("drag ended");
});
const uploadFile = () => {
  console.log("file added uploading");
  files = fileInput.files;
  var formData = new FormData();
  formData.append('filesend',files[0])
  document.getElementById('uploadfilebtn').click();
};

function showmsg(txt){
  msgdiv.innerText=txt;
  msgdiv.classList.add('show');
  setTimeout(function(){msgdiv.classList.remove('show')},5000);
};


setTimeout(function(){document.getElementsByClassName('msg')[0].classList.remove('show')},5000)