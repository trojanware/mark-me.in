$(document).ready(function(){ 
window.addEventListener('load',loadPercentage,true);
	update = false;
	user = $('#user')[0].innerHTML;
	$("input").click(function (event){
		var src = event.target.id;
		var subs = src.substring(0,3);
		var subject = src.substring(3,src.length);		
		//alert(subs);
		user = $('#user')[0].innerHTML;
		day = $('#day')[0].innerHTML;
		$.get('/updateData/',{'user':user,'day':day,'subject':subject,"checked":subs},function (rep){
			//alert('sub name = '+rep['subject']);
			//$('#total'+rep['subject'])[0].innerHTML = rep['total'];
			//$('#absent'+rep['subject'])[0].innerHTML = rep['absent'];			
			var present = rep['present'];
			var total = rep['total'];
			percent = (present/total)*100;
			//setPercentage(rep);		
			strper = percent.toString();
			index = strper.indexOf('.');
			if(index!=-1)
				$('#percent'+rep['subject'])[0].innerHTML = strper.substring(0,5);
			else
				$('#percent'+rep['subject'])[0].innerHTML = percent.toString();
			//alert("index = "+strper[4]);	
			//$('#percent'+rep['subject'])[0].innerHTML = (percent.toString());
		});
	});
	$('#btnUpdate').mousedown(function (){
		$('#btnUpdate').css("opacity","0.9");
	});
	$('#btnUpdate').mouseup(function (){
		$('#btnUpdate').css("opacity","1.0");
	});
	$('#btnUpdate').bind('click',function () {
		$.get('/logout/',{'user':user},function () {
			location.href = '/home/';
		});
	});
	/*$('#btnUpdate').bind('mouseenter',function(e) {
		$("<div id=\"floatDiv\">{{user}}</div>").insertAfter('#day');
		var src = e.target.id;
		//var tag = $('#'+src)[0];
		var offset = $(this).offset();
		var left = offset.left;
		var top = offset.top;
		//alert("left = "+left);		
		$('#floatDiv').css('position','fixed');		
		$('#floatDiv').css('top',top+30);
		$('#floatDiv').css('left',left+30);
	});*/
	
	$('#btnUpdate').mouseleave(function() {
		$('#floatDiv').empty();
	});
	$('.subjName').bind('mouseenter',function(e) {
		var src = e.target.id;
		$("<div id=\"floatDiv\"><p id=\"lblTotal\"></p><p id=\"lblPresent\"></p><p id=\"lblAbsent\"></p></div>").insertAfter('#day');		
		var offset = $(this).offset();
		var left = offset.left;
		var top = offset.top;
		$('#floatDiv').css('position','fixed');		
		$('#floatDiv').css('top',top+30);
		$('#floatDiv').css('left',left+50);
		$('#floatDiv').css('border',"2px solid");
		$('#floatDiv').css('z-index',"2");
		
		fetchData(src);
	});
	$('.subjName').bind('mouseleave',function(e) {
		$('#floatDiv').css('border',"0px");
		$('#floatDiv').empty();
	});
	
	$('#btnChange').bind('click',function (){
		var lstTags = $('.subj');		
		for(var i=0;i<lstTags.length;i++) {
			//var offset = $('.subj').offset();
			var id = lstTags[i].innerHTML;
			//alert(id);
			$('<input type=\"text\" class=\"txtchange\" id=\"chng'+id+'\" />').appendTo('#change');
			$('#chng'+id).val(id);
		}

	});
});

	function loadPercentage(){
		user = $('#user')[0].innerHTML;		
		$.get('/getPercentage/',{'user':user},function (rep){
			for(var k=0;k<rep.length;k++) {
				nm = '#percent'+rep[k]['name'];				
				if(!rep[k]['total']==0){
					percent = (parseInt(rep[k]['present'])/parseInt(rep[k]['total']))*100;
					strper = percent.toString();
					index = strper.indexOf('.');
					if(index!=-1)
						$(nm)[0].innerHTML = strper.substring(0,4);
					else
						$(nm)[0].innerHTML = percent;
			//alert("index = "+strper[4]);									
				}
				else{					
					$(nm)[0].innerHTML ="00.00";}
				if(parseFloat($(nm)[0].innerHTML)<75)
					$(nm).css('background-color','#ff0000');
			}
		});
	}
function fetchData(subjname){	
	//alert("name = "+subjname+"user = "+user);
	$.get('/fetchData/',{'user':user,'name':subjname},function(rep){
		$('#lblTotal')[0].innerHTML = "Total Classes : "+rep['total']
		$('#lblPresent')[0].innerHTML = "Present: "+rep['present']
		$('#lblAbsent')[0].innerHTML = "Absent: "+rep['absent']
	});
}

/*function setPercentage(rep){
	$.get('/setPercentage/',{'subject':rep['subject'],'percent':percent,'user':rep['user']},function(reply){
	});
}*/
