function setTab(name,cursel){
	cursel_0=cursel;
	for(var i=1; i<=links_len; i++){
		var menu = document.getElementById(name+i);
		var menudiv = document.getElementById("con_"+name+"_"+i);
		if(i==cursel){
			menu.className="off";
			menudiv.style.display="block";
		}
		else{
			menu.className="";
			menudiv.style.display="none";
		}
	}
}
var name_0='one';
var cursel_0=1;
var links_len;
onload=function(){
	var links = document.getElementById("containerForm").getElementsByTagName('li')
	links_len=links.length;
	setTab(name_0,cursel_0);
}