var dropZone = document.querySelector(".drop-zone");
var fileInput = document.querySelector("#fileInput");
var browseBtn = document.querySelector("#browseBtn");
var msgdiv = document.querySelector("#msgbox");
var maxSize = 50 * 1024 * 1024; 

browseBtn.addEventListener('click',function(){
  fileInput.click();
});

function passint(){
  if(window.confirm('Set password to your file !?')==false){
    document.getElementById('pass').value='none';
  }else{
    var password=prompt('Please enter the password !?');
    document.getElementById('pass').value=password;;
  };
};

fileInput.addEventListener('change',function(){
  passint();
  document.getElementById('uploadfilebtn').click();
});

dropZone.addEventListener("drop", function(e){
  e.preventDefault();
  const files = e.dataTransfer.files;
  if (files.length == 1) {
    if (files[0].size < maxSize) {
      fileInput.files = files;
      passint();
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
  showmsg('Please wait while uploading...')
};

function showmsg(txt){
  msgdiv.innerText=txt;
  msgdiv.classList.add('show');
  setTimeout(function(){msgdiv.classList.remove('show')},5000);
};


function likes(){
  let name=prompt('Please Enter your name!![for like]')
  $.ajax({
    type: 'POST',
    url: "{% url 'home' %}",
    data: {
      csrfmiddlewaretoken: '{{ csrf_token }}',
      'name':name,
    },
    success: function() {
      var s = document.getElementById('likno').innerText;
      document.getElementById('likno').innerText = Number(s) + 1;
    },
  });
};

function downl(btn){
var pass=prompt('Please enter the password: ')
if(pass.length=='0'){
  showmsg('Please enter password')
}else{
$.ajax({
  type:'GET',
  url:'/download/',
  data:{
      file_id:btn.id,
      password:pass,
  },
  success:function(res){
  if(String(res).includes('/')){
    const link = document.createElement('a');
    link.href =res;
    link.setAttribute('download','');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }else{
    showmsg(res);
  };
  },
})
}
}

function view(btn){
var pass=prompt('Please enter the password: ')
if(pass.length=='0'){
  showmsg('Please enter password')
}else{
$.ajax({
  type:'GET',
  url:'/viewcheck/',
  data:{
      file_id:btn.id,
      password:pass,
  },
  success:function(res){
  if(String(res).includes('/')){
    window.location.href=res
  }else{
    showmsg(res);
  };
  },
})
}
}

function deletcheck(btn){
var pass=prompt('Please enter the password: ')
if(pass.length=='0'){
  showmsg('Please enter password')
}else{
  $.ajax({
  type:'GET',
  url:'/deletcheck/',
  data:{
    file_id:btn.id,
    password:pass,
  },
  success:function(res){
    if(String(res).includes('/')){
      window.location.href=res
    }else{
      showmsg(res);
    };
  },
  })
  };
}

function play(){
  var duration=(document.getElementById('audiomain').duration)/60;
  document.getElementById('audiomain').play();
  document.getElementById('play1').style.display='none';
  document.getElementById('play2').style.display='block';
  document.getElementById('detl').innerText='Playing the Song🎵🎶 ['+String(Math.round(duration))+' min]';
};
function pause(){
  var duration=(document.getElementById('audiomain').duration)/60;
  document.getElementById('audiomain').pause();
  document.getElementById('play2').style.display='none';
  document.getElementById('play1').style.display='block';
  document.getElementById('detl').innerText='Paused the Song⏸['+String(Math.round(duration))+' min]';
};
setTimeout(function(){document.getElementsByClassName('msg')[0].classList.remove('show')},5000);
