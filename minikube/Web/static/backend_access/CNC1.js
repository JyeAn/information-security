
function data_set(data){
    buf = data[0]['data'];
    document.getElementById("relative_x").innerText=buf['relative_coordinate']['x'];
    document.getElementById("relative_y").innerText=buf['relative_coordinate']['y'];
    document.getElementById("relative_z").innerText=buf['relative_coordinate']['z'];
    document.getElementById("absolute_x").innerText=buf['absolute_coordinate']['x'];
    document.getElementById("absolute_y").innerText=buf['absolute_coordinate']['y'];
    document.getElementById("absolute_z").innerText=buf['absolute_coordinate']['z'];
    document.getElementById("f").innerText=buf['other']['f'];
    document.getElementById("process_num").innerText=buf['other']['process_time'];
    document.getElementById("running_time").innerText=buf['other']['running_time'];
    document.getElementById("cycle_time").innerText=buf['other']['cycle_time'];
    document.getElementById("machine_x").innerText=buf['machine_coordinate']['x'];
    document.getElementById("machine_y").innerText=buf['machine_coordinate']['y'];
    document.getElementById("machine_z").innerText=buf['machine_coordinate']['z'];
    document.getElementById("momentum_x").innerText=buf['momentum']['x'];
    document.getElementById("momentum_y").innerText=buf['momentum']['y'];
    document.getElementById("momentum_z").innerText=buf['momentum']['z'];
    if ( buf['block_b']['b1'] ) document.getElementById("svg1").className="panelImg light";
    else document.getElementById("svg1").className="panelImg";
    if ( buf['block_b']['b2'] ) document.getElementById("svg2").className="panelImg light";
    else document.getElementById("svg2").className="panelImg";
    if ( buf['block_b']['b3'] ) document.getElementById("svg3").className="panelImg light";
    else document.getElementById("svg3").className="panelImg";
    if ( buf['block_b']['b4'] ) document.getElementById("svg4").className="panelImg light";
    else document.getElementById("svg4").className="panelImg";
    if ( buf['block_b']['b5'] ) document.getElementById("svg5").className="panelImg light";
    else document.getElementById("svg5").className="panelImg";
    if ( buf['block_b']['b6'] ) document.getElementById("svg6").className="panelImg light";
    else document.getElementById("svg6").className="panelImg";
    if ( buf['block_b']['b7'] ) document.getElementById("svg7").className="panelImg light";
    else document.getElementById("svg7").className="panelImg";
    if ( buf['block_b']['b8'] ) document.getElementById("svg8").className="panelImg light";
    else document.getElementById("svg8").className="panelImg";
    if ( buf['block_d']['d1'] ) document.getElementById("svg9").className="panelImg light";
    else document.getElementById("svg9").className="panelImg";
    if ( buf['block_d']['d2'] ) document.getElementById("svg10").className="panelImg light";
    else document.getElementById("svg10").className="panelImg";
    if ( buf['block_d']['d3'] ) document.getElementById("svg11").className="panelImg light";
    else document.getElementById("svg11").className="panelImg";
    if ( buf['block_d']['d4'] ) document.getElementById("svg12").className="panelImg light";
    else document.getElementById("svg12").className="panelImg";
    if ( buf['block_d']['d5'] ) document.getElementById("svg13").className="panelImg light";
    else document.getElementById("svg13").className="panelImg";
    if ( buf['block_d']['d6'] ) document.getElementById("svg14").className="panelImg light";
    else document.getElementById("svg14").className="panelImg";
    document.getElementById("m1").innerText=buf['block_m']['m1'];
    document.getElementById("m2").innerText=buf['block_m']['m2'];
    if ( buf['block_a']['a1'] ) document.getElementById("svg15").className="panelImg light";
    else document.getElementById("svg15").className="panelImg";
    if ( buf['block_a']['a2'] ) document.getElementById("svg16").className="panelImg light";
    else document.getElementById("svg16").className="panelImg";
    if ( buf['block_c']['c1'] ) document.getElementById("svg17").className="panelImg light";
    else document.getElementById("svg17").className="panelImg";
    if ( buf['block_c']['c2'] ) document.getElementById("svg18").className="panelImg light";
    else document.getElementById("svg18").className="panelImg";
    if ( buf['block_c']['c3'] ) document.getElementById("svg19").className="panelImg light";
    else document.getElementById("svg19").className="panelImg";
    if ( buf['block_c']['c4'] ) document.getElementById("svg20").className="panelImg light";
    else document.getElementById("svg20").className="panelImg";
    if ( buf['block_c']['c5'] ) document.getElementById("svg21").className="panelImg light";
    else document.getElementById("svg21").className="panelImg";
    if ( buf['block_c']['c6'] ) document.getElementById("svg22").className="panelImg light";
    else document.getElementById("svg22").className="panelImg";
    if ( buf['block_c']['c7'] ) document.getElementById("svg23").className="panelImg light";
    else document.getElementById("svg23").className="panelImg";
    if ( buf['block_e']['e1'] ) document.getElementById("svg24").className="panelImg light";
    else document.getElementById("svg24").className="panelImg";
    if ( buf['block_e']['e2'] ) document.getElementById("svg25").className="panelImg light";
    else document.getElementById("svg25").className="panelImg";
    if ( buf['block_e']['e3'] ) document.getElementById("svg26").className="panelImg light";
    else document.getElementById("svg26").className="panelImg";
    if ( buf['block_e']['e4'] ) document.getElementById("svg27").className="panelImg light";
    else document.getElementById("svg27").className="panelImg";
    if ( buf['block_e']['e5'] ) document.getElementById("svg28").className="panelImg light";
    else document.getElementById("svg28").className="panelImg";
    if ( buf['block_e']['e6'] ) document.getElementById("svg29").className="panelImg light";
    else document.getElementById("svg29").className="panelImg";
    document.getElementById("m3").innerText=buf['block_m']['m3'];
    document.getElementById("m4").innerText=buf['block_m']['m4'];
    if ( buf['block_a']['a3'] ) document.getElementById("svg30").className="panelImg light";
    else document.getElementById("svg30").className="panelImg";
    if ( buf['block_a']['a4'] ) document.getElementById("svg31").className="panelImg light";
    else document.getElementById("svg31").className="panelImg";
    if ( buf['block_c']['c8'] ) document.getElementById("svg32").className="panelImg light";
    else document.getElementById("svg32").className="panelImg";
    if ( buf['block_c']['c9'] ) document.getElementById("svg33").className="panelImg light";
    else document.getElementById("svg33").className="panelImg";
    if ( buf['block_c']['c10'] ) document.getElementById("svg34").className="panelImg light";
    else document.getElementById("svg34").className="panelImg";
    if ( buf['block_c']['c11'] ) document.getElementById("svg35").className="panelImg light";
    else document.getElementById("svg35").className="panelImg";
    if ( buf['block_c']['c12'] ) document.getElementById("svg36").className="panelImg light";
    else document.getElementById("svg36").className="panelImg";
    document.getElementById("m6").innerText=buf['block_m']['m6'];
    if ( buf['block_f']['f1'] ) document.getElementById("svg37").className="panelImg light";
    else document.getElementById("svg37").className="panelImg";
    if ( buf['block_f']['f2'] ) document.getElementById("svg38").className="panelImg light";
    else document.getElementById("svg38").className="panelImg";
    if ( buf['block_f']['f3'] ) document.getElementById("svg39").className="panelImg light";
    else document.getElementById("svg39").className="panelImg";
    if ( buf['block_f']['f4'] ) document.getElementById("svg40").className="panelImg light";
    else document.getElementById("svg40").className="panelImg";
    if ( buf['block_f']['f5'] ) document.getElementById("svg41").className="panelImg light";
    else document.getElementById("svg41").className="panelImg";
    if ( buf['block_f']['f6'] ) document.getElementById("svg42").className="panelImg light";
    else document.getElementById("svg42").className="panelImg";
    if ( buf['block_f']['f7'] ) document.getElementById("svg43").className="panelImg light";
    else document.getElementById("svg43").className="panelImg";
    document.getElementById("m5").innerText=buf['block_m']['m5'];
    if ( buf['block_h']['h1'] ) document.getElementById("svg44").className="panelImg_sm light";
    else document.getElementById("svg44").className="panelImg_sm";
    if ( buf['block_h']['h2'] ) document.getElementById("svg45").className="panelImg_sm light";
    else document.getElementById("svg45").className="panelImg_sm";
    if ( buf['block_h']['h3'] ) document.getElementById("svg46").className="panelImg_sm light";
    else document.getElementById("svg46").className="panelImg_sm";
    if ( buf['block_h']['h4'] ) document.getElementById("svg47").className="panelImg_sm light";
    else document.getElementById("svg47").className="panelImg_sm";
    if ( buf['block_i']['i1'] ) document.getElementById("svg48").className="panelImg_sm light";
    else document.getElementById("svg48").className="panelImg_sm";
    if ( buf['block_i']['i2'] ) document.getElementById("svg49").className="panelImg_sm light";
    else document.getElementById("svg49").className="panelImg_sm";
    if ( buf['block_i']['i3'] ) document.getElementById("svg50").className="panelImg_sm light";
    else document.getElementById("svg50").className="panelImg_sm";
    if ( buf['block_i']['i4'] ) document.getElementById("svg51").className="panelImg_sm light";
    else document.getElementById("svg51").className="panelImg_sm";
    if ( buf['block_i']['i5'] ) document.getElementById("svg52").className="panelImg_sm light";
    else document.getElementById("svg52").className="panelImg_sm";
    if ( buf['block_i']['i6'] ) document.getElementById("svg53").className="panelImg_sm light";
    else document.getElementById("svg53").className="panelImg_sm";
    document.getElementById("m7").innerText=buf['block_m']['m7'];
    if ( buf['block_g']['g1'] ) document.getElementById("svg54").className="panelImg light";
    else document.getElementById("svg54").className="panelImg";
    if ( buf['block_g']['g2'] ) document.getElementById("svg55").className="panelImg light";
    else document.getElementById("svg55").className="panelImg";
    if ( buf['block_g']['g3'] ) document.getElementById("svg56").className="panelImg light";
    else document.getElementById("svg56").className="panelImg";
    if ( buf['block_g']['g4'] ) document.getElementById("svg57").className="panelImg light";
    else document.getElementById("svg57").className="panelImg";
    if ( buf['block_g']['g5'] ) document.getElementById("svg58").className="panelImg light";
    else document.getElementById("svg58").className="panelImg";
}

const fetchAPI = async () => {
    try {
      
      var response = await fetch("https://test2.ntut-smodist.tw/get_CNC1");
  
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
  
