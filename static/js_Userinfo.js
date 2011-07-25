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
		
		id = $('#id_user').html();		
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

tt = [];
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
	cbxid = '#op'+shortF;
	$(cbxid).remove();
	subsDay = {};
	subsDay["day"] = shortF;
	for(var j = 1;j<i;j++){
		str = $('#txt'+j).val().trim();
		if(str!=""){
			hr = "Hour"+j;
			subsDay[hr] = str;			
		}
	}
	tt.push(subsDay);
	//Reset all the text fields
	for(var j=1;j<i;j++){	
		txtid = "#txt"+j;			
		$(txtid).val('');
	}
}

subjects = new Array();
function btnFinishHandler(){	
		$('<div id=\"loading\">Loading...</div>').insertAfter('#header_strip');
		$.get('/registerUser/',{'coll':coll,'branch':branch,'sem':sem,'sec':sec,'usn':usn,'id':id,'tt':$.toJSON(tt)},function(rep){
			user = rep['user'];			
			location.href = "/details/";
			//$('#loading').css('background-color','#ffffff');
			node = document.getElementById('loading');
			parent = node.parentNode;
			parent.removeChild(document.getElementById('loading'));
			//$('#loading').empty();
		});			
}
