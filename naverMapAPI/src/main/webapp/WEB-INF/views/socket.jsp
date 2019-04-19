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
<script>
$(function(){
	if(!window.WebSocket){
		alert('웹 소켓을 지원하지 않는 브라우저 입니다.');
		return;
	}
	
	var socket = new WebSocket("ws://localhost:8080/map/echo");
	
	socket.onopen = function(){
		console.log('접속 성공');
		socket.send('Hello');
	}
	
	socket.onclose = function(){
		console.log('접속 해제');
	}
	
	socket.onmessage = function(msg){
		console.log('데이터 수신 : ', msg.data);
		allMsg = $('#recv-message').html();
		allMsg = msg.data + '<br>' + allMsg;
		$('#recv-message').html(allMsg);
	}
	
	socket.onerror = function(err){
		console.log("에러", err);
	}
	
	$('#send-btn').click(function(){
		var msg = $('#send-message').val();
		socket.send(msg);
	})
});
</script>
<title>Insert title here</title>
</head>
<body>
	<h1>웹 소켓 테스트</h1>
	<div>
		전송 메시지 :
		<input type="text" id="send-message">
		<button type="button" id="send-btn">전송</button>
	</div>
	
	<div>
		수신 메시지 : <span id="recv-message"></span>
	</div>
</body>
</html>