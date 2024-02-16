let parent = document.getElementById("map");
let demo = parent.getElementById("agv");
function data_set(data){
    x = data[0]['x'];
    y = data[0]['y'];
    demo.setAttribute('x',x);
    demo.setAttribute('y',y);
}

const fetchAPI = async () => {
    try {
      
      var response = await fetch("https://test2.ntut-smodist.tw/get_AGV");
  
      if (response.status === 200) {
        var js_data = await response.json();
        data_set(js_data);
      } else {
        console.log('請求異常');
      }
    } catch (err) {
      console.log(err);
    }
  };
setInterval(function() {
    fetchAPI();
}, 500);
  
