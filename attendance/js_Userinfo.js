var i=1;
user = "test2";
$(document).ready(function () {
	$('#basic-info').css('color','#ff0000');	
	$('#btnCon').bind('click',function () {
		coll = ($('#Coll').val()).trim();
		branch = $('#txtBranch').val();
		sem = $('#txtSem').val();
		sec = $('#txtSec').val();	
		usn = $('#txtUsn').val();
		$('#stage1').empty();
		$('#tt').css('color','#ff0000');	
		$('#basic-info').css('color','#000000');
		$('.heading')[0].innerHTML = 'Time Table';		
		
		var id = $('#id_user').html();		
		/*$.get('/registerUser/',{'coll':coll,'branch':branch,'sem':sem,'sec':sec,'usn':usn,'id':id},function(rep){
			user = rep['user'];
		});*/
		populateWorkspace();		
		$("<div class=\"myBtn\" id=\"btnFinish\">Finish</div>").insertAfter('#btnCon');
		parent = document.getElementById('btnCon').parentNode;
		parent.removeChild(document.getElementById("btnCon"));
		$('#btnFinish').bind('click',function () {
			btnFinishHandler();
		});
	});		
});

tt = []
function populateWorkspace(){
	$('Day: <select id=cbxDays></select><br /><div id=\"subjs\"></div>').appendTo('#stage1');	
	for(i=1;i<=3;i++)
		$('<p>Hour '+i+': <input type=\"text\" id=\"txt'+i+'\" /></p>').appendTo('#subjs');	
		$('<div class=myBtn id=btnNext>Next Day>></div><br /><br />').insertAfter('#subjs');
		$('<div class=myBtn id=btnMore>More>></div><br /><br />').insertAfter('#subjs');
		$('#btnNext').bind('click',function () {			
			updateTT();
		});
		$('#btnMore').bind('click',function () {
		var limit = i+2;
		for(;i<=limit;i++)
			$('<p>Hour '+i+': <input type=\"text\" id=\"txt'+i+'\" /></p>').appendTo('#subjs');					
	});	
	$('<option id="opMon">Monday</option><option id="opTue">Tuesday</option><option id="opWed">Wednesday</option><option id="opThu">Thursday</option><option id="opFriday">Friday</option><option id="opSat">Saturday</option><option id="opSun">Sunday</option>').appendTo('#cbxDays');
}

function updateTT(){
	var day = $('#cbxDays').val();
	var shortF = day.substring(0,3);
	var subsDay = {'day':shortF};
	for(var j = 1;j<i;j++){
		str = $('#txt'+j).val().trim();
		if(str!=""){
			hr = "Hour"+j;
			subsDay[hr] = str;			
			//alert(subsDay
		}
	}
	tt.push(subsDay);
}

subjects = new Array();
function btnFinishHandler(){	
	$.get('/getTT/',{'tt':$.toJSON(tt),'user':user},function (rep){	
		alert('user = '+rep['noSubjects']);
		for(var j = 1;j<=rep['noSubjects'];j++){
			strKey = "hour"+j;
			subjects.push(rep[strKey]);
			alert(rep[strKey]);
		}
	});
	$.get('/checkUser/',{},function(rep){
		//alert("is logged in = "+rep['reply']);
	});
}
