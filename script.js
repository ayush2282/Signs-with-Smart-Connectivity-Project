
async function load(){
 let r=await fetch('/api/data');
 let d=await r.json();
 document.getElementById('box').innerHTML=
 `Weather:${d.weather}<br>Speed:${d.speed} km/h<br>Traffic:${d.traffic}`;
}
load();
