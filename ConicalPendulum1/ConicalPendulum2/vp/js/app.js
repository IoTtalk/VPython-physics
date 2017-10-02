/*==JS VERSION 1==*/
//var endPoint = window.location.origin + '/';
var endPoint = 'http://140.113.199.199:9999/'
var timestamp = '';

const csmRegister = function(pf) {
  id += btoa(random()).substring(1, 10);
  if (pf.is_sim == undefined){
    pf.is_sim = false;
  }
  if (pf.d_name == undefined){
    pf.d_name = (floor(Math.random() * 99)).toString() + '.' + pf.dm_name ;
  }
  $.ajax({
    url: endPoint + id,
    type: 'POST',
    data: JSON.stringify({profile: pf}),
    //dataType: 'json',
    contentType: 'application/json',
    success: function () {
      document.title = pf.d_name;
      window.onunload = csmDelete;
      window.onbeforeunload = csmDelete;
      window.onclose = csmDelete;
      window.onpagehide = csmDelete;
    },
    error: function (a,b,c) { 
      alert('register fail');
    }
  }).done(function(){
        csmPush ('__Ctl_I__',['SET_DF_STATUS_RSP',{'cmd_params':[]}])
  });
};


const csmPull = function(df, handler) {
  var value = null;
  var preHandler = function(data) {
    if (data.samples.length > 0 && data.samples[0][0] != timestamp) {
      timestamp = data.samples[0][0];
      if (data.samples[0][1].length == 1) {
        value = data.samples[0][1][0];
      }
      else {
        value = data.samples[0][1];
      }
      console.log(value)
    }
    handler(value);
  }
  $.ajax({
    url: endPoint + id + '/' + df,
    type: 'GET',
    error: function(a, b, c) {handler(value);}
  })
  .done(preHandler);
};

const csmPush = function (df, rawData) {
  jsonData = {'data': rawData};
  $.ajax({
    url: endPoint + id + '/' + df,
    type: 'PUT',
    data: JSON.stringify(jsonData),
    dataType: 'json',
    contentType: 'application/json'
  })
};

const csmDelete = function() {
  $.ajax({
    url: endPoint + id,
    type: 'DELETE'
  })
};

/*==JS VERSION 2==*/
var id = 'VPython';
var project = window.location.hash.replace(/^#/,'');

function dai (profile) {
  var df_func = profile.df_list;
  profile.df_list = [];

  for (var i = 0; i < 12; i++) {
    id += '0123456789abcdef'[Math.floor(Math.random() * 16)];
  }
  if (profile.is_sim == undefined) {
    profile.is_sim = false;
  }
  if (profile.d_name == undefined) {
    profile.d_name =  (floor(Math.random() * 99)).toString() +'.'+ profile.dm_name;
  }
  
  for (var i = 0 ; i < df_func.length ; i++) {
    profile.df_list.append(df_func[i].name);
  }

  function initCallback (result) {
    console.log('register:', result);
    document.title = profile.d_name;
  }

  function pull (df_name, data) {
    if (df_name == 'Control') {
      if (data[0] == 'SET_DF_STATUS') {
        dan.push('Control', ['SET_DF_STATUS_RSP', data[1]], function (res) {});
      }
    }
    else {
      for (var i = 0 ; i < df_func.length ; i++) {
        if (df_func[i].name == df_name) {
          df_func[i](data);
          break;
        }
      }
    }
  }

  window.onunload = dan.deregister;
  window.onbeforeunload = dan.deregister;
  window.onclose = dan.deregister;
  window.onpagehide = dan.deregister;

  dan.init(pull, csmapi.get_endpoint(), id, profile, initCallback);
};

/*==Basic==*/
var audio = {}

const preloadAudio = function(filename) {
  if (audio[filename] == undefined) {
    audio[filename] = new Audio('/da/vp/audio/' + filename);
  }
};

const playAudio = function(filename) {
  preloadAudio(filename);
  if (audio[filename] != undefined) {
    audio[filename].play();
  }
};

const execute = function (code) {
  const options = {
    lang: 'vpython',
    version: 2.1
  };

  const js_code = glowscript_compile(code, options);
  const program = eval(js_code);

  //console.log(js_code);
  program(function(err){
    console.log(err)
  });
};

const fetch_code = function(url){
  $.get(url)
   .done(function (data) {
     execute(data);
   })
   .fail(function (jqxhr, settings, execption) {
     console.log(execption);
  });
};

window.__context = {
  glowscript_container: $('#glowscript'),
};

var originHash;
$(function () {
  originHash = window.location.hash;
  fetch_code('vp/py/'+ Project + '.py');
});

$(window).on('hashchange', function (a) {
  if (window.location.hash != originHash) {
    window.location.hash = originHash;
  }
});
