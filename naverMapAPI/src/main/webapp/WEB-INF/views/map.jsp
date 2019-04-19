<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=rbeyz68rf5&submodules=geocoder"></script>
<script>
$(function(){
	if(!window.WebSocket){
		alert('웹 소켓을 지원하지 않는 브라우저 입니다.');
		return;
	}
	
	var mapOptions = {
		center: new naver.maps.LatLng(37.5666805, 126.9784147),
		zoom: 10
		/* scaleControl: false,
		logoControl: false,
		mapDataControl: false,
		zoomControl: true,
		zoomControlOptions: {
			style: naver.maps.ZoomControlStyle.SMALL
		} */
	};
	
	var map = new naver.maps.Map('map', mapOptions);
	
	var marker = new naver.maps.Marker({
		position: new naver.maps.LatLng(37.5666805, 126.9784147),
		map: map
	});
	
	var socket = new WebSocket("ws://localhost:8080/map/car");
	
	socket.onopen = function(){
		console.log('접속 성공');
		msg = JSON.stringify({
				"msgType": "POSITION_SUB",
				"target": 1
		});
		socket.send(msg);
	}
	
	socket.onmessage = function(msg){
		console.log('데이터 수신 : ', msg.data);
		msgInfo = JSON.parse(msg.data)
		if(msgInfo.msgType=="POSITION"){
			position = new naver.maps.LatLng(msgInfo.lat, msgInfo.lng);
			marker.setPosition(position);
			map.setCenter(position); 
		}
	}
	
	socket.onclose = function(){
		console.log('접속 해제');
	}
	
	socket.onerror = function(err){
		console.log("에러", err);
	}
	
	$('.direction').click(function(){
		direction = $(this).data('direction')
		msg = JSON.stringify({
			msgType: "CONTROL",
			target: 1,
			direction: direction 	
		});
		socket.send(msg);
	})
	//var cityhall = new naver.maps.LatLng(37.5666805, 126.9784147);
	//사용자 마커 아이콘 설정
/* 	var markerIcon = {
		url : '${contextPath}/resources/images/marker.png',
		size : new naver.maps.Size(32, 32),
		origin: new naver.maps.Point(0, 0),
		anchor : new naver.maps.Point(16, 32)
	};
	var marker = new naver.maps.Marker({
		position: cityhall,
		map: map
	});
	
	contentString = 
	`<div style = "padding:5px">
		<img src="${contextPath}/resources/images/cityhall.jpg" /><br/>
		"${items}"
	</div>`;
	
	var infowindow = new naver.maps.InfoWindow({
		content: contentString
	}); */
	
	//클릭 이벤트 핸들러
/* 	naver.maps.Event.addListener(map, 'click', function(e){
		if(infowindow.getMap()){
			infowindow.close();
		} else {
			infowindow.open(map, marker);
		}
	});
	
	naver.maps.Service.geocode(
			{address: '역삼'},
			function(status, response){
				console.log(status, response)
				if(status === naver.maps.Service.Status.ERROR){
					return alert('Something wrong!');
				}
				var result = response.result,
				items = result.items;
				
				console.log(items);
			}
	);
	naver.maps.Service.reverseGeocode({
		location: new naver.maps.LatLng(37.5666805, 126.9784147),
		},
		function(status, response){
			if (status !== naver.maps.Service.Status.OK){
				return alert('Something wrong!');
			}
			
			var result = response.result,
				items = result.items;
			console.log(items);
		}
	);

	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(
				onSuccessGeolocation,
				onErrorGeolocation);
	} else {
		return alert('Something wrong!');
	}
	
	function onSuccessGeolocation(position){
		var location = new naver.maps.LatLng(position.coords.latitude,
											position.coords.longitude);
		
		var marker = new naver.maps.Marker({
			position: location,
			map: map
		});
		
		map.setCenter(location);
		map.setZoom(12);
	}
	
	function onErrorGeolocation(){
		alert('실패');
	} */
	

	//1초에 한번씩 마커 움직이면서 중심 같이 이동	
/*  	setInterval(function(){
 		
 		marker.position._lat += 0.0001;
 		marker.position._lng += 0.0001;
 		
 		var nextPosition = new naver.maps.LatLng(marker.position._lat, marker.position._lng);
 		marker.setPosition(nextPosition);
		map.setCenter(nextPosition); 		

	}, 1000); */
	
});
</script>
<title>Insert title here</title>
</head>
<body>
<div class="mx-auto" style="width:500px">
<h1>원격 조정</h1>
<div id="map" style="width:80%; height:400px;"></div>

<div class="mt-5">
	<table>
		<tr>
			<td></td>
			<td>
				<button class="direction" data-direction="UP">
				<i class="fas fa-angle-up"></i>
				</button>
			</td>
			<td></td>
		</tr>
		<tr>
			<td>
				<button class="direction" data-direction="LEFT">
				<i class="fas fa-angle-left"></i>
				</button>
			</td>
			<td></td>
			<td>
				<button class="direction" data-direction="RIGHT">
				<i class="fas fa-angle-right"></i>
				</button>
			</td>
		</tr>
		<tr>
			<td></td>
			<td>
				<button class="direction" data-direction="DOWN">
				<i class="fas fa-angle-down"></i>
				</button>
			</td>
			<td style="width:70px;"></td>
		</tr>
	</table>
</div>

</div>
</body>
</html>